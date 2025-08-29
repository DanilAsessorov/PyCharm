from datetime import datetime


def filter_by_state(transaction_list: list, state: str = 'EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
       state
        соответствует указанному значению"""
    return [x for x in transaction_list if x['state'] == state]


transaction = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(transaction))


def sort_by_date(transaction_list: list, reverse: bool = True) -> list:
    """ Функция, которая принимает список словарей и необязательный параметр,
        задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
         новый список, отсортированный по дате (date)."""
    return sorted(transaction_list, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)


transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
print(sort_by_date(transactions))
