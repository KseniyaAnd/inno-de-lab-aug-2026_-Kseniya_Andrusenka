-- ТЕСТ 2: Попытка INSERT без соответствующих прав
-- Под hr_user пробуем добавить запись
INSERT INTO Employees (FirstName, LastName, Department, Salary) 
VALUES ('Frank', 'Miller', 'HR', 61000.00);

-- РЕЗУЛЬТАТ ТЕСТА 2: Ошибка.