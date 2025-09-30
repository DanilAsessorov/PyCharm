import logging
import os
from typing import Union

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def get_masks_logger() -> logging.Logger:
    masks_logger = logging.getLogger("masks")
    masks_logger.setLevel(logging.DEBUG)

    log_file = os.path.join(LOG_DIR, "masks.log")

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    if not any(
        isinstance(h, logging.FileHandler) and h.baseFilename == os.path.abspath(log_file)
        for h in masks_logger.handlers
    ):
        masks_logger.addHandler(file_handler)

    return masks_logger


logger = get_masks_logger()


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция принимает на вход номер карты в виде
    числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX."""
    logger.info(f"masks: маскирование номера карты {card_number}")
    card_number = str(card_number)
    if card_number.isdigit() and len(card_number) == 16:
        mask_number = f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[12:]}"
        return mask_number
    logger.error("masks: некорректный ввод номера карты")
    return "Некорректный ввод"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX."""
    logger.info(f"masks: маскирование номера счета {account_number}")
    account_number = str(account_number)

    if account_number.isdigit() and len(account_number) >= 4:
        mask_account = f"**{account_number[-4:]}"
        return mask_account

    logger.error("masks: некорректный ввод номера счета")
    return "Некорректный ввод"


def main():
    # Пример вызовов, чтобы логи попали в файл
    card = get_mask_card_number("4111111111111111")
    account = get_mask_account("3900123456789012")
    logger.info(f"Masked card: {card}")
    logger.info(f"Masked account: {account}")


if __name__ == "__main__":
    main()
