from src.bank_process import process_bank_search
from src.external_api import convert_to_rub
from src.processing import filter_by_state, sort_by_date
from src.transaction import read_transactions_from_csv, read_transactions_from_excel
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

if __name__ == "__main__":

    def main():
        """отвечает за основную логику проекта и связывает функциональности между собой"""
        transaction_data = []  # Инициализируем переменную перед использованием

        while True:
            print(
                """
            Программа: Привет! Добро пожаловать в программу работы
            с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
            """
            )
            users_input = int(input("Введите нужную цифру:   "))
            if users_input in [1, 2, 3]:
                break

        if users_input == 1:
            transaction_data = load_transactions(r"data\operations.json")
        elif users_input == 2:
            transaction_data = read_transactions_from_csv(r"data\transactions.csv")
        elif users_input == 3:
            transaction_data = read_transactions_from_excel(r"data\transactions_excel.xlsx")

        print(
            """
            Программа: Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
        )

        while True:
            users_input = input("Введите статус:   ").upper()
            if users_input in ["EXECUTED", "CANCELED", "PENDING"]:
                break
            print(f"Программа: Статус операции {users_input} недоступен. ")

        # Фильтрация транзакций по статусу
        transaction_data = filter_by_state(transaction_data, state=users_input)

        print("Программа: Отсортировать операции по дате? Да/Нет")
        users_input1 = input("Сделайте выбор:   ").upper()
        if users_input1 == "ДА":
            while True:
                print("Программа: Отсортировать по возрастанию (1) или по убыванию (2)?")
                users_input2 = int(input("Поставьте необходимое число:   "))
                if users_input2 in [1, 2]:
                    break
            if users_input2 == 1:
                transaction_data = sort_by_date(transaction_data, reverse=True)
            else:
                transaction_data = sort_by_date(transaction_data, reverse=False)

        print("Программа: Выводить только рублевые транзакции? Да/Нет")
        users_input3 = input("Сделайте выбор:   ").upper()
        if users_input3 == "ДА":
            code_currency = "RUB"
            print(f"код валюты {code_currency}")
            # Фильтрация только рублевых транзакций
            transaction_data = [
                txn for txn in transaction_data if txn["operationAmount"]["currency"]["code"] == code_currency
            ]

        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        users_input4 = input("Сделайте выбор:   ").upper()

        if users_input4 == "ДА":
            users_input5 = input("Введите слово:   ")
        else:
            users_input5 = "перевод"

        transaction_data = process_bank_search(transaction_data, search_string=users_input5)
        total_bank_transaction = len(transaction_data)
        print(f"Всего банковских операций в выборке: {total_bank_transaction}")

        for i in transaction_data:
            operation_id = i.get("date")
            di = get_date(operation_id)
            fromi = i.get("from")
            toi = i.get("to")
            icur = i["operationAmount"]["currency"]["code"]
            iammount = i["operationAmount"]["amount"]

            # Создаем словарь для передачи в convert_to_rub
            transaction = {"amount": iammount, "currency": icur}

            print(
                f"""
                {di} {i['description']}
                {mask_account_card(fromi)} - > {mask_account_card(toi)}
                {convert_to_rub(transaction)}  # Передаем словарь вместо отдельных аргументов
                """
            )

    main()  # Запуск функции main
