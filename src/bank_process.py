import re
from collections import Counter


def process_bank_search(data_operation: list[dict], search_string: str) -> list[dict]:
    """функцию, принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    result = []
    re_pattern = re.compile(search_string, re.IGNORECASE)
    for idata in data_operation:
        if re_pattern.search(str(idata.get("description", ""))):
            result.append(idata)
    return result


def process_bank_operations(data_operation: list[dict], categories_user: list) -> dict:
    """функция, принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в категории."""
    count_categories = []
    for idata in data_operation:
        if idata.get("description", "") in categories_user:
            count_categories.append(idata.get("description", ""))
    return dict(Counter(count_categories))
