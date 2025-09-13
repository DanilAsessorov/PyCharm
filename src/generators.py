from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[Any, Any]], currency_name: str) -> Iterator[Dict[Any, Any]]:
    """Функция принимает на вход список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)"""
    if not transactions:
        raise ValueError("Введите транзакцию")

    filtered_transactions = [
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("name") == currency_name
    ]

    if not filtered_transactions:
        raise ValueError("Нет такой транзакции")

    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(transactions: List[Dict[Any, Any]]) -> Iterator[str]:
    """Функция-генератор принимает на вход список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    if not transactions:
        raise ValueError("Список транзакций пуст")

    for transaction in transactions:
        # Формируем строку описания транзакции
        description = transaction.get("description", "").strip()

        if description:
            yield description
        else:
            raise ValueError("Некоторые транзакции не содержат описания")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Функция-генератор генерирует номера банковских карт в заданном диапазоне."""
    for number in range(start, end + 1):
        # Формируем строку номера карты с ведущими нулями и форматируем её
        card_number = f"{number:016d}"
        formatted_card_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_card_number
