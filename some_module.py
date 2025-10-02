import logging

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str) -> str:
    masked = card_number[:6] + "*" * (len(card_number) - 10) + card_number[-4:]
    logger.info(f"Masking card number: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    masked = account_number[:4] + "*" * (len(account_number) - 4)
    logger.info(f"Masking account: {masked}")
    return masked
