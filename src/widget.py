from datetime import datetime


def mask_account_card(card_type_number: str) -> str:
    card_type_number = str(card_type_number)  # Преобразование к строке
    card_info = card_type_number.rsplit(" ", 1)
    if not card_type_number or len(card_type_number.split()) < 2:
        return "введены некорректные данные"
    avg_number = "** ****"
    return f"{card_info[0]} {card_info[1][:4]} {card_info[1][4:6]}{avg_number} {card_info[1][-4:]}"


print(mask_account_card("Visa Platinum 7020792289606361"))


def get_date(iso_date: str) -> str:
    """Преобразует дату в 'ДД.ММ.ГГГГ'"""

    return datetime.fromisoformat(iso_date).strftime("%d.%m.%Y")
