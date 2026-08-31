MAX_RENTAL_BATCH_LIMIT = 150.0


def calculate_rental_batch(
    quantity: int,
    rental_rate: float,
    discount: float = 0.0
) -> tuple[float, bool]:
    """Рассчитывает стоимость партии арендованных дисков.

    Стоимость рассчитывается с учетом количества дисков, стоимости аренды
    одного диска и предоставленной скидки. После расчета проверяется,
    превышает ли итоговая сумма установленный лимит.

    Args:
        quantity: Количество дисков в партии.
        rental_rate: Стоимость аренды одного диска.
        discount: Скидка в виде десятичной дроби. Например, 0.1 означает
            скидку 10%. По умолчанию скидка отсутствует.

    Returns:
        Кортеж из двух значений:
        - final_sum: Итоговая стоимость партии, округленная до 2 знаков.
        - is_limit_exceeded: True, если итоговая стоимость превышает
          MAX_RENTAL_BATCH_LIMIT, иначе False.
    """
    final_sum = round(
        quantity * rental_rate * (1 - discount),
        2
    )

    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded


# === ТЕСТОВЫЕ ВЫЗОВЫ ===

# Вызов с позиционными аргументами
batch_1 = calculate_rental_batch(30, 2.99)

# Вызов с именованными аргументами
batch_2 = calculate_rental_batch(
    quantity=40,
    rental_rate=4.99,
    discount=0.10
)

batch_3 = calculate_rental_batch(10, 1.99)

batch_4 = calculate_rental_batch(
    quantity=50,
    rental_rate=3.50,
    discount=0.20
)


print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

print(
    f"Партия 1 (Academy Dinosaur): "
    f"Сумма {batch_1[0]}$. "
    f"Превышение лимита: {batch_1[1]}"
)

print(
    f"Партия 2 (Affair Prejudice): "
    f"Сумма {batch_2[0]}$. "
    f"Превышение лимита: {batch_2[1]}"
)

print(
    f"Партия 3 (Agent Truman): "
    f"Сумма {batch_3[0]}$. "
    f"Превышение лимита: {batch_3[1]}"
)

print(
    f"Партия 4 (African Egg): "
    f"Сумма {batch_4[0]}$. "
    f"Превышение лимита: {batch_4[1]}"
)