from src.bank_process import process_bank_operations, process_bank_search
from tests.conftest import transaction


def test_process_bank_search(transaction):
    assert process_bank_search(transaction, "орг") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_process_bank_search_dump():
    assert process_bank_search([], "орг") == []


def test_process_bank_operations(transaction):
    assert process_bank_operations(transaction, ["Перевод организации", "Перевод с карты на карту"]) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }
