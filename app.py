import os
import threading
from datetime import date, datetime

from dotenv import load_dotenv
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   url_for)
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///attendance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'ganti-ini-dengan-secret-key-aman')

db = SQLAlchemy(app)


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class Setting(db.Model):
    __tablename__ = 'settings'
    key = db.Column(db.String(50), primary_key=True)
    value = db.Column(db.Text, default='')


class Class(db.Model):
    __tablename__ = 'classes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    grade = db.Column(db.Integer, nullable=False)
    students = db.relationship('Student', backref='kelas', lazy='dynamic',
                               order_by='Student.name')

    @property
    def student_count(self):
        return self.students.count()

    def attendance_today(self):
        today = date.today()
        return (Attendance.query
                .join(Student)
                .filter(Student.class_id == self.id,
                        Attendance.date == today)
                .count())

    def is_submitted_today(self):
        return self.attendance_today() >= self.student_count


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    nis = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(1), default='L')
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'), nullable=False)
    parent_name = db.Column(db.String(100), default='')
    parent_phone = db.Column(db.String(20), default='')
    attendances = db.relationship('Attendance', backref='student', lazy='dynamic')

    def attendance_on(self, check_date):
        return self.attendances.filter_by(date=check_date).first()


class Attendance(db.Model):
    __tablename__ = 'attendances'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(1), nullable=False)  # H=Hadir I=Izin S=Sakit A=Alpha
    notes = db.Column(db.String(200), default='')
    recorded_at = db.Column(db.DateTime, default=datetime.utcnow)
    wa_sent = db.Column(db.Boolean, default=False)

    STATUS_LABELS = {'H': 'Hadir', 'I': 'Izin', 'S': 'Sakit', 'A': 'Alpha'}
    STATUS_COLORS = {'H': 'success', 'I': 'warning', 'S': 'info', 'A': 'danger'}

    @property
    def status_label(self):
        return self.STATUS_LABELS.get(self.status, self.status)

    @property
    def status_color(self):
        return self.STATUS_COLORS.get(self.status, 'secondary')


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_setting(key, default=''):
    s = Setting.query.get(key)
    return s.value if s else default


@app.context_processor
def inject_globals():
    try:
        return {'school_name': get_setting('school_name', 'Aplikasi Absensi')}
    except Exception:
        return {'school_name': 'Aplikasi Absensi'}


def set_setting(key, value):
    s = Setting.query.get(key)
    if s:
        s.value = value
    else:
        s = Setting(key=key, value=value)
        db.session.add(s)
    db.session.commit()


def send_wa_background(attendance_ids):
    """Send WhatsApp notifications in a background thread."""
    from whatsapp import send_notification
    with app.app_context():
        token = get_setting('fonnte_token')
        school_name = get_setting('school_name', 'Sekolah Kami')
        notify_hadir = get_setting('notify_hadir', 'false') == 'true'

        for att_id in attendance_ids:
            att = Attendance.query.get(att_id)
            if not att or att.wa_sent:
                continue
            if att.status == 'H' and not notify_hadir:
                continue
            student = att.student
            if not student.parent_phone:
                continue
            success = send_notification(token, att, student, school_name)
            if success:
                att.wa_sent = True
                db.session.commit()


# ---------------------------------------------------------------------------
# Routes – Dashboard
# ---------------------------------------------------------------------------

@app.route('/')
def dashboard():
    today = date.today()
    total_students = Student.query.count()
    total_classes = Class.query.count()

    counts = {'H': 0, 'I': 0, 'S': 0, 'A': 0}
    rows = (db.session.query(Attendance.status, db.func.count())
            .filter(Attendance.date == today)
            .group_by(Attendance.status)
            .all())
    for status, cnt in rows:
        counts[status] = cnt

    total_recorded = sum(counts.values())
    pct = round(total_recorded / total_students * 100) if total_students else 0

    classes = Class.query.order_by(Class.grade, Class.name).all()
    submitted = [c for c in classes if c.is_submitted_today()]
    pending = [c for c in classes if not c.is_submitted_today()]

    return render_template('dashboard.html',
                           today=today,
                           total_students=total_students,
                           total_classes=total_classes,
                           counts=counts,
                           total_recorded=total_recorded,
                           pct=pct,
                           submitted=submitted,
                           pending=pending)


# ---------------------------------------------------------------------------
# Routes – Classes
# ---------------------------------------------------------------------------

@app.route('/classes')
def classes():
    today = date.today()
    all_classes = Class.query.order_by(Class.grade, Class.name).all()
    return render_template('classes.html', classes=all_classes, today=today)


# ---------------------------------------------------------------------------
# Routes – Attendance
# ---------------------------------------------------------------------------

@app.route('/attendance/<int:class_id>', methods=['GET', 'POST'])
def attendance(class_id):
    kelas = Class.query.get_or_404(class_id)
    today = date.today()
    att_date_str = request.args.get('date', today.isoformat())
    try:
        att_date = date.fromisoformat(att_date_str)
    except ValueError:
        att_date = today

    students = kelas.students.order_by(Student.name).all()

    if request.method == 'POST':
        att_date_post = date.fromisoformat(request.form.get('att_date', today.isoformat()))
        new_ids = []

        for student in students:
            status = request.form.get(f'status_{student.id}', 'H')
            notes = request.form.get(f'notes_{student.id}', '')

            existing = student.attendances.filter_by(date=att_date_post).first()
            if existing:
                existing.status = status
                existing.notes = notes
                existing.wa_sent = False
                att_obj = existing
            else:
                att_obj = Attendance(student_id=student.id, date=att_date_post,
                                     status=status, notes=notes)
                db.session.add(att_obj)
            db.session.flush()
            new_ids.append(att_obj.id)

        db.session.commit()

        t = threading.Thread(target=send_wa_background, args=(new_ids,), daemon=True)
        t.start()

        flash(f'Absensi kelas {kelas.name} tanggal {att_date_post.strftime("%d %B %Y")} '
              f'berhasil disimpan. Notifikasi WhatsApp sedang dikirim.', 'success')
        return redirect(url_for('attendance', class_id=class_id,
                                date=att_date_post.isoformat()))

    existing_att = {}
    for student in students:
        att = student.attendances.filter_by(date=att_date).first()
        if att:
            existing_att[student.id] = att

    return render_template('attendance.html',
                           kelas=kelas,
                           students=students,
                           att_date=att_date,
                           existing_att=existing_att,
                           today=today)


@app.route('/history')
def history():
    class_id = request.args.get('class_id', type=int)
    att_date_str = request.args.get('date', date.today().isoformat())
    try:
        att_date = date.fromisoformat(att_date_str)
    except ValueError:
        att_date = date.today()

    all_classes = Class.query.order_by(Class.grade, Class.name).all()

    query = (db.session.query(Attendance)
             .join(Student)
             .filter(Attendance.date == att_date))

    if class_id:
        query = query.filter(Student.class_id == class_id)

    records = query.order_by(Student.name).all()

    counts = {'H': 0, 'I': 0, 'S': 0, 'A': 0}
    for r in records:
        counts[r.status] = counts.get(r.status, 0) + 1

    return render_template('history.html',
                           records=records,
                           att_date=att_date,
                           all_classes=all_classes,
                           selected_class=class_id,
                           counts=counts)


# ---------------------------------------------------------------------------
# Routes – Students
# ---------------------------------------------------------------------------

@app.route('/students')
def students():
    class_id = request.args.get('class_id', type=int)
    search = request.args.get('q', '').strip()
    all_classes = Class.query.order_by(Class.grade, Class.name).all()

    query = Student.query
    if class_id:
        query = query.filter_by(class_id=class_id)
    if search:
        query = query.filter(Student.name.ilike(f'%{search}%'))

    student_list = query.order_by(Student.name).all()
    return render_template('students.html',
                           students=student_list,
                           all_classes=all_classes,
                           selected_class=class_id,
                           search=search)


@app.route('/students/new', methods=['GET', 'POST'])
def student_new():
    all_classes = Class.query.order_by(Class.grade, Class.name).all()
    if request.method == 'POST':
        nis = request.form['nis'].strip()
        if Student.query.filter_by(nis=nis).first():
            flash('NIS sudah terdaftar.', 'danger')
        else:
            s = Student(
                nis=nis,
                name=request.form['name'].strip(),
                gender=request.form.get('gender', 'L'),
                class_id=int(request.form['class_id']),
                parent_name=request.form.get('parent_name', '').strip(),
                parent_phone=request.form.get('parent_phone', '').strip(),
            )
            db.session.add(s)
            db.session.commit()
            flash(f'Murid {s.name} berhasil ditambahkan.', 'success')
            return redirect(url_for('students'))
    return render_template('student_form.html', student=None, all_classes=all_classes)


@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def student_edit(student_id):
    student = Student.query.get_or_404(student_id)
    all_classes = Class.query.order_by(Class.grade, Class.name).all()
    if request.method == 'POST':
        nis = request.form['nis'].strip()
        conflict = Student.query.filter(Student.nis == nis, Student.id != student_id).first()
        if conflict:
            flash('NIS sudah digunakan murid lain.', 'danger')
        else:
            student.nis = nis
            student.name = request.form['name'].strip()
            student.gender = request.form.get('gender', 'L')
            student.class_id = int(request.form['class_id'])
            student.parent_name = request.form.get('parent_name', '').strip()
            student.parent_phone = request.form.get('parent_phone', '').strip()
            db.session.commit()
            flash(f'Data {student.name} berhasil diperbarui.', 'success')
            return redirect(url_for('students'))
    return render_template('student_form.html', student=student, all_classes=all_classes)


@app.route('/students/<int:student_id>/delete', methods=['POST'])
def student_delete(student_id):
    student = Student.query.get_or_404(student_id)
    Attendance.query.filter_by(student_id=student_id).delete()
    db.session.delete(student)
    db.session.commit()
    flash(f'Murid {student.name} berhasil dihapus.', 'success')
    return redirect(url_for('students'))


# ---------------------------------------------------------------------------
# Routes – Reports
# ---------------------------------------------------------------------------

@app.route('/reports')
def reports():
    all_classes = Class.query.order_by(Class.grade, Class.name).all()
    class_id = request.args.get('class_id', type=int)
    month = request.args.get('month', date.today().strftime('%Y-%m'))

    try:
        year, mon = map(int, month.split('-'))
    except ValueError:
        year, mon = date.today().year, date.today().month

    from calendar import monthrange
    _, days_in_month = monthrange(year, mon)
    start = date(year, mon, 1)
    end = date(year, mon, days_in_month)

    students_query = Student.query
    if class_id:
        students_query = students_query.filter_by(class_id=class_id)
    student_list = students_query.order_by(Student.name).all()

    att_map = {}
    if student_list:
        student_ids = [s.id for s in student_list]
        records = (Attendance.query
                   .filter(Attendance.student_id.in_(student_ids),
                           Attendance.date >= start,
                           Attendance.date <= end)
                   .all())
        for r in records:
            att_map[(r.student_id, r.date)] = r

    return render_template('reports.html',
                           students=student_list,
                           all_classes=all_classes,
                           selected_class=class_id,
                           month=month,
                           year=year, mon=mon,
                           days_in_month=days_in_month,
                           start=start, end=end,
                           att_map=att_map)


# ---------------------------------------------------------------------------
# Routes – Settings
# ---------------------------------------------------------------------------

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        set_setting('school_name', request.form.get('school_name', '').strip())
        set_setting('fonnte_token', request.form.get('fonnte_token', '').strip())
        set_setting('notify_hadir', 'true' if request.form.get('notify_hadir') else 'false')
        set_setting('wa_message_hadir', request.form.get('wa_message_hadir', '').strip())
        set_setting('wa_message_izin', request.form.get('wa_message_izin', '').strip())
        set_setting('wa_message_sakit', request.form.get('wa_message_sakit', '').strip())
        set_setting('wa_message_alpha', request.form.get('wa_message_alpha', '').strip())
        flash('Pengaturan berhasil disimpan.', 'success')
        return redirect(url_for('settings'))

    current = {
        'school_name': get_setting('school_name', 'SD Negeri Contoh'),
        'fonnte_token': get_setting('fonnte_token', ''),
        'notify_hadir': get_setting('notify_hadir', 'false') == 'true',
        'wa_message_hadir': get_setting('wa_message_hadir',
            'Yth. Bapak/Ibu {parent_name},\n\nKami informasikan bahwa putra/putri Anda:\n'
            'Nama: {student_name}\nKelas: {class_name}\nTanggal: {date}\n\n'
            'Status: *HADIR* di sekolah.\n\nTerima kasih.\n*{school_name}*'),
        'wa_message_izin': get_setting('wa_message_izin',
            'Yth. Bapak/Ibu {parent_name},\n\nKami informasikan bahwa putra/putri Anda:\n'
            'Nama: {student_name}\nKelas: {class_name}\nTanggal: {date}\n\n'
            'Status: *IZIN* (tidak hadir dengan keterangan izin).\n\n'
            'Catatan: {notes}\n\nTerima kasih.\n*{school_name}*'),
        'wa_message_sakit': get_setting('wa_message_sakit',
            'Yth. Bapak/Ibu {parent_name},\n\nKami informasikan bahwa putra/putri Anda:\n'
            'Nama: {student_name}\nKelas: {class_name}\nTanggal: {date}\n\n'
            'Status: *SAKIT* (tidak hadir karena sakit).\n\n'
            'Semoga lekas sembuh. Terima kasih.\n*{school_name}*'),
        'wa_message_alpha': get_setting('wa_message_alpha',
            'Yth. Bapak/Ibu {parent_name},\n\nKami informasikan bahwa putra/putri Anda:\n'
            'Nama: {student_name}\nKelas: {class_name}\nTanggal: {date}\n\n'
            'Status: *ALPHA* (tidak hadir tanpa keterangan).\n\n'
            'Mohon segera menghubungi pihak sekolah.\nTerima kasih.\n*{school_name}*'),
    }
    return render_template('settings.html', s=current)


# ---------------------------------------------------------------------------
# API – Resend notification
# ---------------------------------------------------------------------------

@app.route('/api/resend/<int:att_id>', methods=['POST'])
def resend_notification(att_id):
    att = Attendance.query.get_or_404(att_id)
    att.wa_sent = False
    db.session.commit()
    t = threading.Thread(target=send_wa_background, args=([att_id],), daemon=True)
    t.start()
    return jsonify({'ok': True, 'message': 'Notifikasi sedang dikirim ulang'})


@app.route('/api/summary')
def api_summary():
    today = date.today()
    counts = {'H': 0, 'I': 0, 'S': 0, 'A': 0}
    rows = (db.session.query(Attendance.status, db.func.count())
            .filter(Attendance.date == today)
            .group_by(Attendance.status).all())
    for s, c in rows:
        counts[s] = c
    return jsonify(counts)


# ---------------------------------------------------------------------------
# Init DB
# ---------------------------------------------------------------------------

def init_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
