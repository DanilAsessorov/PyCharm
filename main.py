from logger_config import logger
from some_module import get_mask_account, get_mask_card_number
from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))


def main():
    # Пример вызовов, чтобы логи попали в файл
    card = get_mask_card_number("4111111111111111")
    account = get_mask_account("3900123456789012")
    logger.info(f"Masked card: {card}")
    logger.info(f"Masked account: {account}")


if __name__ == "__main__":
    main()
