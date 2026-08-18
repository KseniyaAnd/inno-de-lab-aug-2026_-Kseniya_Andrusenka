-- ТЕСТ 3: Проверка прав INSERT и UPDATE после их предоставления

-- Тест INSERT:
INSERT INTO Employees (FirstName, LastName, Department, Salary) 
VALUES ('Frank', 'Miller', 'HR', 61000.00);
-- РЕЗУЛЬТАТ ТЕСТА 3 (INSERT): Успешно. Строка добавлена.

-- Тест UPDATE:
UPDATE Employees 
SET Salary = 63000.00 
WHERE FirstName = 'Frank' AND LastName = 'Miller';
-- РЕЗУЛЬТАТ ТЕСТА 3 (UPDATE): Успешно. Зарплата сотрудника обновлена.