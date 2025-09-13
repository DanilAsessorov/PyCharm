import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(currency_test_list, currency_done_test_list, currency_no_usd, zero_list):
    with pytest.raises(ValueError) as exc_currency_info:
        list(filter_by_currency(zero_list, "USD"))
    assert str(exc_currency_info.value) == "Введите транзакцию"

    with pytest.raises(ValueError) as exc_currency_info:
        list(filter_by_currency(currency_no_usd, "USD"))
    assert str(exc_currency_info.value) == "Нет такой транзакции"

    assert list(filter_by_currency(currency_test_list, "USD")) == currency_done_test_list


@pytest.mark.parametrize(
    "transactions, expected_output, should_raise",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Покупка в магазине"},
                {"description": "Снятие наличных"},
            ],
            ["Перевод организации", "Покупка в магазине", "Снятие наличных"],
            False,
        ),
        (
            [{"description": "Перевод организации"}, {"description": ""}, {"description": "Снятие наличных"}],
            None,
            True,
        ),
        ([], None, True),
    ],
)
def test_transaction_descriptions(transactions, expected_output, should_raise: bool):
    if should_raise:
        with pytest.raises(ValueError):
            list(transaction_descriptions(transactions))
    else:
        assert list(transaction_descriptions(transactions)) == expected_output


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (0, 2, ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected):
    # Генерируем номера карт
    generated_numbers = list(card_number_generator(start, end))
    # Проверяем, что сгенерированные номера соответствуют ожидаемым
    assert generated_numbers == expected
