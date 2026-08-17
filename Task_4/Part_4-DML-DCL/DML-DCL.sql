-- 1. Увеличить Salary всех сотрудников в отделе 'HR' на 10%.
UPDATE Employees
SET Salary = Salary * 1.10
WHERE Department = 'HR';


-- 2. Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'. 
UPDATE Employees
SET Department = 'Senior IT'
WHERE Salary > 70000.00;


-- 3. Удалить всех сотрудников, которые не назначены ни на один проект в таблице EmployeeProjects. Подсказка: Используйте подзапрос NOT EXISTS или LEFT JOIN
DELETE FROM Employees
WHERE NOT EXISTS (
    SELECT 1 
    FROM EmployeeProjects 
    WHERE EmployeeProjects.EmployeeID = Employees.EmployeeID
);


-- 4.  В рамках одной транзакции, вставить новый проект и назначить на него двух существующих сотрудников с определенным количеством HoursWorked в EmployeeProjects.
BEGIN;

-- Вставляем новый проект
INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('Data Warehouse Migration', 120000.00, '2023-07-01', '2023-12-31');

-- Назначаем двух существующих сотрудников 
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES 
    (1, (SELECT ProjectID FROM Projects WHERE ProjectName = 'Data Warehouse Migration'), 90),
    (2, (SELECT ProjectID FROM Projects WHERE ProjectName = 'Data Warehouse Migration'), 110);

COMMIT;