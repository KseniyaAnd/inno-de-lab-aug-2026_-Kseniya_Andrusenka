-- 1. Вставить двух новых сотрудников в таблицу Employees (с любыми отделами, кроме 'IT').  
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES
('Frank', 'Miller', 'Marketing', 55000.00),
('Grace', 'Wilson', 'Finance', 67000.00);


-- 2. Выбрать всех сотрудников из таблицы Employees.
SELECT *
FROM Employees;


-- 3. Выбрать только FirstName и LastName сотрудников из отдела 'IT'.
SELECT FirstName, LastName
FROM Employees
WHERE Department = 'IT';


-- 4. Обновить Salary 'Alice Smith' до 65000.00.
UPDATE Employees
SET Salary = 65000.00
WHERE FirstName = 'Alice'
  AND LastName = 'Smith';


-- 5. Удалить сотрудника 'Eve Davis'.
DELETE FROM Employees
WHERE FirstName = 'Eve'
  AND LastName = 'Davis';


-- 6. Проверить все изменения, используя SELECT * FROM Employees;.
SELECT *
FROM Employees;