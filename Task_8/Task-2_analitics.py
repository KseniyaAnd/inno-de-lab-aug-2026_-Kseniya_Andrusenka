import time
from typing import Any, Callable


PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Измеряет время выполнения переданной функции.

    Args:
        func: Функция, время выполнения которой необходимо измерить.

    Returns:
        Обёрнутая функция, которая измеряет время выполнения
        оригинальной функции и возвращает её результат.
    """

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = round(
            end_time - start_time,
            TIME_DECIMALS
        )

        print(
            f"{PERFORMANCE_LOG_PREFIX} "
            f"Функция '{func.__name__}' выполнена "
            f"за {execution_time} сек."
        )

        return result

    return wrapper


@performance_logger
def get_sorted_report(
    revenue_data: list[dict[str, str | float]]
) -> list[dict[str, str | float]]:
    """Сортирует данные о выручке жанров по убыванию.

    Args:
        revenue_data: Список словарей с данными о выручке жанров.
            Каждый словарь содержит название категории и общую выручку.

    Returns:
        Отсортированный список словарей по убыванию значения total_sales.
    """

    return sorted(
        revenue_data,
        key=lambda item: item["total_sales"],
        reverse=True
    )


# Набор 1 (Стандартный)
data_1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]


# Набор 2 (С одинаковой выручкой)
data_2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]


# Набор 3 (Единичный элемент)
data_3 = [
    {"category": "Drama", "total_sales": 500.00}
]


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")


print("--- ТЕСТ 1 ---")

report_1 = get_sorted_report(data_1)

print("Топ категорий по выручке:")

for index, item in enumerate(report_1, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


print("--- ТЕСТ 2 ---")

report_2 = get_sorted_report(data_2)

print("Топ категорий по выручке:")

for index, item in enumerate(report_2, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")


print("--- ТЕСТ 3 ---")

report_3 = get_sorted_report(data_3)

print("Топ категорий по выручке:")

for index, item in enumerate(report_3, start=1):
    print(f"{index}. {item['category']}: {item['total_sales']}")