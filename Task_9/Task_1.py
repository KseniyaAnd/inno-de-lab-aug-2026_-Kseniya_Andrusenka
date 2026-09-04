class Trainee:
    """Представляет обычного стажёра с именем, фамилией и текущим количеством баллов."""

    def __init__(
        self,
        name: str,
        surname: str,
        score: int = 0,
        passing_grade: int = 10
    ) -> None:
        """Инициализирует стажёра и задаёт его начальные параметры."""
        self.name: str = name
        self.surname: str = surname
        self.passing_grade: int = passing_grade
        self.__score: int = score

    @property
    def score(self) -> int:
        """Возвращает текущее количество баллов стажёра."""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        """Устанавливает количество баллов с проверкой переданного значения."""
        # Количество баллов должно быть целым числом.
        if not isinstance(value, int):
            raise ValueError(
                f"Expected value of type int, got {type(value)}"
            )

        # Количество баллов не может быть отрицательным.
        if value < 0:
            raise ValueError(
                "The score shouldn't be less than 0!"
            )

        self.__score = value

    def do_homework(self) -> None:
        """Увеличивает количество баллов стажёра за выполненную домашнюю работу."""
        self.score += 1

    def miss_homework(self) -> None:
        """Уменьшает количество баллов стажёра за пропущенную домашнюю работу."""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Увеличивает количество баллов за посещение лекции."""
        self.score += 1

    def miss_lecture(self) -> None:
        """Уменьшает количество баллов за пропуск лекции."""
        self.score -= 1

    def is_passing(self) -> bool:
        """Проверяет, набрал ли стажёр проходное количество баллов."""
        return self.score >= self.passing_grade


# === ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===

trainee = Trainee(
    name="Иван",
    surname="Иванов",
    score=9,
    passing_grade=10
)

trainee.do_homework()
print(
    f"Баллы: {trainee.score}, "
    f"Прошел курс: {trainee.is_passing()}"
)

trainee.miss_lecture()
print(
    f"Баллы: {trainee.score}, "
    f"Прошел курс: {trainee.is_passing()}"
)

try:
    # Пытаемся установить некорректное отрицательное количество баллов.
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")