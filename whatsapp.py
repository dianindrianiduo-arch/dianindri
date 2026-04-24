"""WhatsApp notification via Fonnte API (fonnte.com)."""
import requests
from datetime import date


FONNTE_URL = 'https://api.fonnte.com/send'


def _build_message(template: str, att, student, school_name: str) -> str:
    att_date = att.date if isinstance(att.date, date) else date.today()
    return template.format(
        parent_name=student.parent_name or 'Wali Murid',
        student_name=student.name,
        class_name=student.kelas.name if student.kelas else '',
        date=att_date.strftime('%d %B %Y'),
        status=att.status_label,
        notes=att.notes or '-',
        school_name=school_name,
    )


def send_notification(token: str, att, student, school_name: str) -> bool:
    """Send a WhatsApp notification. Returns True on success."""
    if not token or not student.parent_phone:
        return False

    from app import get_setting

    templates = {
        'H': get_setting('wa_message_hadir'),
        'I': get_setting('wa_message_izin'),
        'S': get_setting('wa_message_sakit'),
        'A': get_setting('wa_message_alpha'),
    }
    template = templates.get(att.status, '')
    if not template:
        return False

    message = _build_message(template, att, student, school_name)

    phone = student.parent_phone.strip().lstrip('+').lstrip('0')
    if not phone.startswith('62'):
        phone = '62' + phone

    try:
        resp = requests.post(
            FONNTE_URL,
            headers={'Authorization': token},
            data={'target': phone, 'message': message, 'countryCode': '62'},
            timeout=15,
        )
        data = resp.json()
        return data.get('status', False) is not False
    except Exception:
        return False
