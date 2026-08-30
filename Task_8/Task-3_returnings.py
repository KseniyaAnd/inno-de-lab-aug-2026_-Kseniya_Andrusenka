from typing import Any


DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
    film_title: str,
    days_overdue: Any,
    fine_rate: float
) -> tuple[float, float] | None:
    """Рассчитывает штраф за просрочку и индекс оборачиваемости.

    Функция обрабатывает некорректные входные данные.
    Она перехватывает ошибки TypeError при передаче неподходящего типа,
    ValueError при невозможности преобразовать значение в число
    и ZeroDivisionError при нулевом количестве дней просрочки.

    Args:
        film_title: Название фильма.
        days_overdue: Количество дней просрочки.
        fine_rate: Размер штрафа за один день просрочки.

    Returns:
        Кортеж из итогового штрафа и индекса оборачиваемости,
        если расчет выполнен успешно. None, если произошла ошибка
        при обработке входных данных.
    """

    try:
        numeric_days = float(days_overdue)

        total_fine = numeric_days * fine_rate

        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        return total_fine, return_index

    except TypeError as error:
        print(
            f"[ОШИБКА ТИПА] Некорректный тип данных "
            f"для '{film_title}': {error}"
        )

    except ValueError as error:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни "
            f"в число для '{film_title}': {error}"
        )

    except ZeroDivisionError as error:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки "
            f"для '{film_title}': {error}"
        )

    finally:
        print("--- Проверка транзакции возврата завершена ---")

    return None


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")


result_1 = calculate_overdue_fine(
    "Matrix",
    5,
    1.5
)

if result_1 is not None:
    total_fine, return_index = result_1
    print(
        f"Фильм: 'Matrix' | "
        f"Итоговый штраф: {total_fine}$ | "
        f"Индекс: {return_index}"
    )


result_2 = calculate_overdue_fine(
    "Inception",
    "пять",
    2.0
)


result_3 = calculate_overdue_fine(
    "Avatar",
    0,
    2.5
)


result_4 = calculate_overdue_fine(
    "Interstellar",
    [3],
    3.0
)