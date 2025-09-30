import json
import logging
import os
from typing import Any, List

# Настройка логирования
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="a", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Создание и установка форматера
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру (проверяем, чтобы обработчик не добавлялся дублирующе)
if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
    logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Any]:
    """Загрузить транзакции из JSON-файла.

    При отсутствии файла вернёт пустой список.
    При ошибке декодирования или некорректной структуре данных вернёт пустой список.
    """
    if not isinstance(file_path, str) or not file_path:
        logger.error("Неверный путь к файлу: путь должен быть непустой строкой.")
        return []

    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
                return []

            if isinstance(data, list):
                logger.info(f"Транзакции успешно загружены из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком.")
                return []
    except OSError as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []
