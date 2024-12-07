from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO

def create_pdf(json_data):
    # Создаем PDF в памяти
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Регистрация шрифта
    pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))
    c.setFont("DejaVuSans", 16)

    # Заголовок
    c.drawString(100, height - 50, f"Персонаж: {json_data['character']['name']}")

    # Основная информация о персонаже
    c.setFont("DejaVuSans", 12)
    y_position = height - 100
    character_info = [
        f"Игрок: {json_data['character']['player']}",
        f"Класс: {json_data['character']['class_name']}",
        f"Уровень: {json_data['character']['level']}",
        f"Раса: {json_data['character']['race']}",
        f"Предыстория: {json_data['character']['background']}",
        f"Мировоззрение: {json_data['character']['alignment']}",
        f"Опыт: {json_data['character']['experience']}",
        f"Заметки: {json_data['character']['notes']}",
    ]

    for line in character_info:
        c.drawString(100, y_position, line)
        y_position -= 20

    # Атрибуты
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Атрибуты:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)
    for attr, values in json_data['character']['attributes'].items():
        c.drawString(120, y_position, f"{attr.capitalize()}: {values['value']} (Модификатор: {values['modifier']})")
        y_position -= 20

    # Навыки
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Навыки:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)
    for skill, values in json_data['character']['skills'].items():
        c.drawString(120, y_position, f"{skill.capitalize()}: {'Да' if values['proficient'] else 'Нет'} (Модификатор: {values['modifier']})")
        y_position -= 20

    # Способности
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Способности:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)
    for ability in json_data['character']['abilities']:
        c.drawString(120, y_position, f"{ability['name']}: {ability['description']}")
        y_position -= 20

    # Заклинания
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Заклинания:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)
    for spell in json_data['character']['spells']:
        c.drawString(120, y_position, f"{spell['name']} (Уровень: {spell['level']}): {spell['description']} (Использования: {spell['uses']})")
        y_position -= 20

    # Оборудование
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Оборудование:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)

    # Оружие
    for weapon in json_data['character']['equipment']['weapons']:
        c.drawString(120, y_position, f"Оружие: {weapon['name']} (Тип: {weapon['type']}, Урон: {weapon['damage']}, Бонус: {weapon['bonus']})")
        y_position -= 20

    # Броня
    armor = json_data['character']['equipment']['armor']
    c.drawString(120, y_position, f"Броня: {armor['name']} (Класс брони: {armor['armorClass']})")
    y_position -= 20

    # Предметы
    for item in json_data['character']['equipment']['items']:
        c.drawString(120, y_position, f"Предмет: {item['name']} - {item['description']}")
        y_position -= 20

    # Здоровье
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Здоровье:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)
    health = json_data['character']['health']
    c.drawString(120, y_position, f"Максимальные очки здоровья: {health['maxHP']}")
    y_position -= 20
    c.drawString(120, y_position, f"Текущие очки здоровья: {health['currentHP']}")
    y_position -= 20
    c.drawString(120, y_position, f"Кубик здоровья: {health['hitDice']}")
    y_position -= 20

    # Класс брони, инициатива и скорость
    c.setFont("DejaVuSans", 14)
    c.drawString(100, y_position, "Дополнительная информация:")
    y_position -= 20
    c.setFont("DejaVuSans", 12)
    c.drawString(120, y_position, f"Класс брони: {json_data['character']['armorClass']}")
    y_position -= 20
    c.drawString(120, y_position, f"Инициатива: {json_data['character']['initiative']}")
    y_position -= 20
    c.drawString(120, y_position, f"Скорость: {json_data['character']['speed']} футов")
    y_position -= 20

    # Завершение PDF
    c.showPage()
    c.save()
    buffer.seek(0)  # Возвращаемся в начало буфера
    return buffer
