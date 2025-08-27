from datetime import datetime


def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    card_info = card_type_number.rsplit(' ', 1)
    avg_number = "** ****"
    return f"{card_info[0]} {card_info[1][:4]} {card_info[1][4:6]}{avg_number} {card_info[1][-4:]}"

print(mask_account_card("Visa Platinum 7020792289606361"))


def get_date(iso_date: str) -> str:

    """Преобразует дату в 'ДД.ММ.ГГГГ'"""

    return datetime.fromisoformat(iso_date).strftime('%d.%m.%Y')