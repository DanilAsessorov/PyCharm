import os

from src.decorators import log, my_function

# Проверка на успешное выполнение функции


def test_my_function_success(capsys):
    result = my_function(4, 2)
    assert result == 6
    captured = capsys.readouterr()
    assert "my_function ок. Результат: 6" in captured.out


# Проверка на вывод в файл


@log(filename="test_log.txt")
def my_function_sum(x, y):
    return x + y


def test_my_function_file_output():
    my_function_sum(2, 3)
    with open("test_log.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert "Функция my_function_sum ок. Результат: 5" in content
    os.remove("test_log.txt")


# Проверка обработки других исключений:


@log()
def my_function_key_error():
    return {"a": 1}["b"]


def test_my_function_key_error(capsys):
    my_function_key_error()
    captured = capsys.readouterr()
    assert "my_function_key_error error: 'b'" in captured.out


# Проверка с разными типами аргументов:


@log()
def my_function_concat(a, b):
    return a + b


def test_my_function_concat_strings(capsys):
    result = my_function_concat("hello", "world")
    assert result == "helloworld"
    captured = capsys.readouterr()
    assert "my_function_concat ок. Результат: helloworld" in captured.out


# Проверка очистки файла:


def test_file_cleanup():
    filename = "test_log_cleanup.txt"

    @log(filename=filename)
    def my_function_cleanup(x):
        return x

    my_function_cleanup(1)
    assert os.path.exists(filename)
    os.remove(filename)
    assert not os.path.exists(filename)
