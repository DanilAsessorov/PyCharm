import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def valid_card_numbers():
    return [
        (1234567890123456, "1234 56 ** **** 3456"),
        (1111222233334444, "1111 22 ** **** 4444"),
    ]

@pytest.fixture
def invalid_card_numbers():
    return [12345, 1234567890, 123456789012345]

@pytest.fixture
def edge_case_card_numbers():
    return [1234, 12345678901234567890]

@pytest.fixture
def valid_account_numbers():
    return [
        (1234567890123456, "**3456"),
        (987654321, "**4321"),
    ]

@pytest.fixture
def invalid_account_numbers():
    return [123, 12]

@pytest.mark.parametrize("card_number, expected", [
    (num, expected) for num, expected in [
        (1234567890123456, "1234 56 ** **** 3456"),
        (1111222233334444, "1111 22 ** **** 4444"),
    ]
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("card_number", [12345, 1234567890, 123456789012345])
def test_get_mask_card_number_invalid_length(card_number):
    assert get_mask_card_number(card_number) == "Некорректный ввод"

@pytest.mark.parametrize("card_number", [1234, 12345678901234567890])
def test_get_mask_card_number_edge_cases(card_number):
    result = get_mask_card_number(card_number)
    assert isinstance(result, str)

@pytest.mark.parametrize("account_number, expected", [
    (num, expected) for num, expected in [
        (1234567890123456, "**3456"),
        (987654321, "**4321"),
    ]
])
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize("account_number", [123, 12])
def test_get_mask_account_invalid(account_number):
    assert get_mask_account(account_number) == "Некорректный ввод"
