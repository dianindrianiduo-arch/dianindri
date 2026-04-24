"""
Seed database with 1062 students across 36 classes (6 grades x 6 classes).
Run once: python seed.py
"""
import random
import sys

from app import app, db, Class, Student, Setting

MALE_FIRST = [
    'Muhammad', 'Ahmad', 'Andi', 'Budi', 'Dani', 'Eko', 'Fajar', 'Galih',
    'Hendra', 'Ilham', 'Joko', 'Kevin', 'Luthfi', 'Mario', 'Nanda', 'Oscar',
    'Putra', 'Rizky', 'Sandi', 'Taufik', 'Wahyu', 'Yoga', 'Zaki', 'Agung',
    'Bagas', 'Candra', 'Dimas', 'Faisal', 'Gilang', 'Hafiz', 'Ivan', 'Jefri',
    'Kelvin', 'Leon', 'Marwan', 'Naufal', 'Okta', 'Pandu', 'Rahman', 'Satria',
    'Tri', 'Umar', 'Vino', 'Widi', 'Yuda', 'Zainal', 'Akbar', 'Bayu',
    'Daffa', 'Erwin', 'Farhan', 'Gery', 'Hadi', 'Indra', 'Jaya', 'Kurnia',
    'Lukman', 'Nabil', 'Prabowo', 'Qodir', 'Salman', 'Toni', 'Yusuf',
    'Zakariya', 'Aditya', 'Bintang', 'Cahyo', 'Derry', 'Fikri', 'Haryanto',
]

FEMALE_FIRST = [
    'Siti', 'Dewi', 'Ayu', 'Bunga', 'Citra', 'Dina', 'Erika', 'Fatima',
    'Gita', 'Hani', 'Indah', 'Jihan', 'Kirana', 'Laila', 'Maya', 'Nadia',
    'Ocha', 'Putri', 'Risa', 'Sari', 'Tari', 'Ulfa', 'Vika', 'Wulan',
    'Yanti', 'Zahra', 'Aulia', 'Bella', 'Caca', 'Devi', 'Elisa', 'Fina',
    'Gina', 'Hana', 'Intan', 'Julia', 'Kartika', 'Lina', 'Mira', 'Nita',
    'Olivia', 'Priska', 'Rani', 'Sintia', 'Tina', 'Vera', 'Widya', 'Yuli',
    'Zara', 'Amelia', 'Berliana', 'Cantika', 'Diah', 'Erlina', 'Fitriani',
    'Ghina', 'Hasna', 'Ika', 'Julianti', 'Kurniati', 'Lestari', 'Mutia',
    'Nurul', 'Paramita', 'Rahma', 'Suci', 'Tasya', 'Ulfah', 'Viona',
]

LAST_NAMES = [
    'Pratama', 'Prasetyo', 'Santoso', 'Wijaya', 'Kusuma', 'Suharto',
    'Setiawan', 'Hartanto', 'Nugraha', 'Saputra', 'Permana', 'Hidayat',
    'Firmansyah', 'Ramadan', 'Kurniawan', 'Andrianto', 'Sulistyo',
    'Purnomo', 'Raharjo', 'Wibowo', 'Susanto', 'Gunawan', 'Wahyudi',
    'Adiputra', 'Hakim', 'Iskandar', 'Jamaludin', 'Kamaludin',
    'Laksana', 'Maulana', 'Nasution', 'Oktavian', 'Purnawan',
    'Rohman', 'Subagyo', 'Triyono', 'Utomo', 'Winarno', 'Yuliono',
    'Zaenuri', 'Arifin', 'Budiman', 'Cahyono', 'Darmawan', 'Effendi',
    'Fauzan', 'Ginting', 'Hasibuan', 'Ibrahim', 'Junaedi',
]

PARENT_FIRST_M = [
    'Bapak Hendra', 'Bapak Ahmad', 'Bapak Joko', 'Bapak Eko', 'Bapak Dani',
    'Bapak Suharto', 'Bapak Wahyu', 'Bapak Agus', 'Bapak Rudi', 'Bapak Budi',
    'Bapak Fajar', 'Bapak Gilang', 'Bapak Hadi', 'Bapak Ivan', 'Bapak Jaya',
]

PARENT_FIRST_F = [
    'Ibu Sri', 'Ibu Dewi', 'Ibu Wati', 'Ibu Sari', 'Ibu Nita',
    'Ibu Indah', 'Ibu Retno', 'Ibu Yanti', 'Ibu Rina', 'Ibu Dina',
    'Ibu Fitri', 'Ibu Hani', 'Ibu Laila', 'Ibu Maya', 'Ibu Nurul',
]

GRADES = [1, 2, 3, 4, 5, 6]
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']


def random_phone():
    prefix = random.choice(['0812', '0813', '0821', '0822', '0831', '0852',
                            '0853', '0857', '0858', '0877', '0878'])
    suffix = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return prefix + suffix


def random_name(gender):
    if gender == 'L':
        first = random.choice(MALE_FIRST)
        parent_first = random.choice(PARENT_FIRST_M + PARENT_FIRST_F)
    else:
        first = random.choice(FEMALE_FIRST)
        parent_first = random.choice(PARENT_FIRST_M + PARENT_FIRST_F)
    last = random.choice(LAST_NAMES)
    return f'{first} {last}', f'{parent_first} {last}'


def seed():
    with app.app_context():
        if Student.query.count() > 0:
            print('Database sudah ada data. Hapus attendance.db dulu jika ingin reset.')
            sys.exit(0)

        db.create_all()

        # Default settings
        defaults = {
            'school_name': 'SD Negeri 1 Contoh',
            'fonnte_token': '',
            'notify_hadir': 'false',
            'wa_message_hadir': (
                'Yth. Bapak/Ibu {parent_name},\n\n'
                'Kami informasikan bahwa putra/putri Anda:\n'
                'Nama  : {student_name}\n'
                'Kelas : {class_name}\n'
                'Tgl   : {date}\n\n'
                'Status: *HADIR* di sekolah.\n\n'
                'Terima kasih.\n*{school_name}*'
            ),
            'wa_message_izin': (
                'Yth. Bapak/Ibu {parent_name},\n\n'
                'Kami informasikan bahwa putra/putri Anda:\n'
                'Nama  : {student_name}\n'
                'Kelas : {class_name}\n'
                'Tgl   : {date}\n\n'
                'Status: *IZIN* (tidak hadir dengan keterangan).\n'
                'Catatan: {notes}\n\n'
                'Terima kasih.\n*{school_name}*'
            ),
            'wa_message_sakit': (
                'Yth. Bapak/Ibu {parent_name},\n\n'
                'Kami informasikan bahwa putra/putri Anda:\n'
                'Nama  : {student_name}\n'
                'Kelas : {class_name}\n'
                'Tgl   : {date}\n\n'
                'Status: *SAKIT* (tidak hadir karena sakit).\n\n'
                'Semoga lekas sembuh. Terima kasih.\n*{school_name}*'
            ),
            'wa_message_alpha': (
                'Yth. Bapak/Ibu {parent_name},\n\n'
                'Kami informasikan bahwa putra/putri Anda:\n'
                'Nama  : {student_name}\n'
                'Kelas : {class_name}\n'
                'Tgl   : {date}\n\n'
                'Status: *ALPHA* (tidak hadir tanpa keterangan).\n\n'
                'Mohon segera hubungi pihak sekolah.\n'
                'Terima kasih.\n*{school_name}*'
            ),
        }
        for k, v in defaults.items():
            if not Setting.query.get(k):
                db.session.add(Setting(key=k, value=v))

        print('Membuat 36 kelas ...')
        classes = []
        for grade in GRADES:
            for letter in LETTERS:
                name = f'{grade}{letter}'
                kelas = Class(name=name, grade=grade)
                db.session.add(kelas)
                classes.append(kelas)
        db.session.flush()

        # 36 classes × mix of 29/30 = 1062 total
        # 18 classes with 30, 18 with 29  →  18×30 + 18×29 = 540+522 = 1062
        sizes = [30] * 18 + [29] * 18
        random.shuffle(sizes)

        print('Membuat 1062 murid ...')
        nis_counter = 2024001
        for kelas, size in zip(classes, sizes):
            for i in range(size):
                gender = 'L' if random.random() < 0.52 else 'P'
                name, parent_name = random_name(gender)
                student = Student(
                    nis=str(nis_counter),
                    name=name,
                    gender=gender,
                    class_id=kelas.id,
                    parent_name=parent_name,
                    parent_phone=random_phone(),
                )
                db.session.add(student)
                nis_counter += 1

        db.session.commit()
        total = Student.query.count()
        print(f'Selesai! {total} murid dari {len(classes)} kelas berhasil dibuat.')


if __name__ == '__main__':
    seed()
