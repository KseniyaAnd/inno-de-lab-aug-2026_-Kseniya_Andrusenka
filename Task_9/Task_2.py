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


class HardworkingTrainee(Trainee):
    """Представляет стажёра, который получает больше баллов за домашнюю работу."""

    def do_homework(self) -> None:
        """Увеличивает количество баллов на два за выполненную домашнюю работу."""
        self.score += 2


class AuditTrainee(Trainee):
    """Представляет стажёра, который проходит обучение без проверки баллов."""

    def is_passing(self) -> bool:
        """Всегда возвращает True, так как аудитор считается прошедшим."""
        return True


class Cohort:
    """Представляет учебную группу, содержащую список стажёров."""

    def __init__(
        self,
        title: str,
        trainees: list[Trainee] | None = None
    ) -> None:
        """Инициализирует учебную группу с названием и списком стажёров."""
        self.title: str = title

        # Если список стажёров не передан, создаём новый пустой список.
        self.trainees: list[Trainee] = (
            trainees if trainees is not None else []
        )

    def add_trainee(self, trainee: Trainee) -> None:
        """Добавляет нового стажёра в учебную группу."""
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """Проводит лекцию для всех стажёров группы."""
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """Возвращает список всех стажёров, прошедших по итогам обучения."""
        return [
            trainee
            for trainee in self.trainees
            if trainee.is_passing()
        ]


# === ПРОВЕРКА ===

std_trainee = Trainee(
    "Алексей",
    "Смирнов",
    score=8,
    passing_grade=10
)

hard_trainee = HardworkingTrainee(
    "Елена",
    "Петрова",
    score=8,
    passing_grade=10
)

audit_trainee = AuditTrainee(
    "Дмитрий",
    "Сидоров",
    score=0,
    passing_grade=10
)


cohort = Cohort("Python Advanced")

cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)


cohort.conduct_lecture()

hard_trainee.do_homework()


passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")

for student in cohort.trainees:
    print(
        f"{student.name} {student.surname} | "
        f"Баллы: {student.score} | "
        f"Проходит: {student.is_passing()}"
    )

print("\nУспешно зачислены на следующий модуль:")

for student in passing_students:
    print(f"- {student.name} {student.surname}")
