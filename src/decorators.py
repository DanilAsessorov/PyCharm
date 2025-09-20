from functools import wraps

"""Декоратор log логирует вызовы функций: пишет результат или сообщение об ошибке в файл или в stdout.
При успехе: записывает/выводит "Функция <имя> ок. Результат: <результат>".
При исключении: записывает/выводит "<имя> error: <тип исключения>. Inputs: <args>, <kwargs>."""


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Функция {name_func} ок. Результат: {result}" + "\n")
                else:
                    print(f"{name_func} ок. Результат: {result}")
                return result
            except Exception as e:
                # Объединяем все исключения в один блок
                result = None
                name_func = func.__name__
                log_message = f"{name_func} error: {type(e).__name__}. Inputs: {args}, {kwargs}. Сообщение: {e}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                return result

        return wrapper

    return decorator


@log(filename="")
# @log(filename="mylog.txt")
def my_function(x, y):
    return x + y
