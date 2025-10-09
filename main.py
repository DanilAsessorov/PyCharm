from src.bank_process import process_bank_search, process_bank_operations
from src.external_api import convert_to_rub
from src.processing import filter_by_state, sort_by_date
from src.transaction import read_transactions_from_csv, read_transactions_from_excel
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

def main():
    """Основная функция, отвечающая за логику программы."""
    transaction_data = []  # Инициализируем переменную перед использованием
    while True:
        print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print(
            """
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
            """
        )
        try:
            users_input = int(input("Введите нужную цифру: "))
            if users_input in [1, 2, 3]:
                break
            else:
                print("Программа: Неправильный ввод. Пожалуйста, введите 1, 2 или 3.")
        except ValueError:
            print("Программа: Неправильный ввод. Пожалуйста, введите число.")

    # Загрузка данных транзакций из выбранного формата
    try:
        if users_input == 1:
            transaction_data = load_transactions(r"data\operations.json")
        elif users_input == 2:
            transaction_data = read_transactions_from_csv(r"data\transactions.csv")
        elif users_input == 3:
            transaction_data = read_transactions_from_excel(r"data\transactions_excel.xlsx")
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return

    # Проверка на пустые данные
    if not transaction_data:
        print("Программа: Нет транзакций для отображения. Попробуйте снова.")
        return

    # Удаление пустых словарей из transaction_data
    transaction_data = [txn for txn in transaction_data if txn]  # Удаляем пустые записи
    print("Содержимое transaction_data после удаления пустых элементов:")
    for transaction in transaction_data:
        print(transaction)

    # Проверка на наличие ключа 'state' в каждой транзакции
    for txn in transaction_data:
        if 'state' not in txn:
            print(f"Ошибка: транзакция без ключа 'state': {txn}")

    print(
        """
        Программа: Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING
        """
    )

    while True:
        users_input = input("Введите статус: ").upper()
        if users_input in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        print(f"Программа: Статус операции {users_input} недоступен.")

    # Фильтрация транзакций по статусу
    transaction_data = filter_by_state(transaction_data, state=users_input)

    print("Транзакции после фильтрации:", transaction_data)

    # Фильтрация транзакций по статусу
    transaction_data = filter_by_state(transaction_data, state=users_input)

    print("Транзакции после фильтрации:", transaction_data)

    print("Программа: Отсортировать операции по дате? Да/Нет")
    users_input1 = input("Сделайте выбор: ").upper()
    if users_input1 == "ДА":
        while True:
            print("Программа: Отсортировать по возрастанию (1) или по убыванию (2)?")
            try:
                users_input2 = int(input("Поставьте необходимое число: "))
                if users_input2 in [1, 2]:
                    break
            except ValueError:
                print("Программа: Пожалуйста, введите 1 или 2.")
        transaction_data = sort_by_date(transaction_data, reverse=users_input2 == 2)

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    users_input3 = input("Сделайте выбор: ").upper()
    if users_input3 == "ДА":
        code_currency = "RUB"
        print(f"Код валюты: {code_currency}")
        transaction_data = [
            txn
            for txn in transaction_data
            if txn.get("operationAmount", {}).get("currency", {}).get("code") == code_currency
        ]

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    users_input4 = input("Сделайте выбор:   ").upper()

    if users_input4 == "ДА":
        users_input5 = input("Введите слово:   ")
    else:
        users_input5 = "перевод"  # Значение по умолчанию, если пользователь не ввел слово

    # Поиск транзакций по описанию
    transaction_data = process_bank_search(transaction_data, search_string=users_input5)
    total_bank_transaction = len(transaction_data)
    print(f"Всего банковских операций в выборке: {total_bank_transaction}")

    # Запрос категорий для подсчета и вывод результатов
    categories = ['Salary', 'Transfer', 'Gift', 'Payment']  # Пример категорий
    operation_counts = process_bank_operations(transaction_data, categories)
    print(f"Количество операций по категориям: {operation_counts}")

    # Вывод информации о транзакциях
    for i in transaction_data:
        operation_id = i.get("date")
        di = get_date(operation_id)
        fromi = i.get("from", "Не указано")
        toi = i.get("to", "Не указано")
        icur = i.get("operationAmount", {}).get("currency", {}).get("code", "Не указано")
        iammount = i.get("operationAmount", {}).get("amount", 0)

        # Создаем словарь для передачи в convert_to_rub
        transaction = {"amount": iammount, "currency": icur}

        try:
            convert_amount = convert_to_rub(transaction)  # Возможна ошибка при конвертации
        except Exception as e:
            print(f"Ошибка при конвертации: {e}")
            convert_amount = "Ошибка"

        print(
            f"""
            {di} {i.get('description', 'Нет описания')}
            {mask_account_card(fromi)} - > {mask_account_card(toi)}
            {convert_amount}
            """
        )

if __name__ == "__main__":
    main()  # Запуск функции main