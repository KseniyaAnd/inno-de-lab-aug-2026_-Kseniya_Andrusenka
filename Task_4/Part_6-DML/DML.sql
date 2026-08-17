-- 1.  Найти ProjectName всех проектов, в которых 'Bob Johnson' работал более 150 часов. 
SELECT p.ProjectName
FROM Projects p
JOIN EmployeeProjects ep ON p.ProjectID = ep.ProjectID
JOIN Employees e ON ep.EmployeeID = e.EmployeeID
WHERE e.FirstName = 'Bob' 
  AND e.LastName = 'Johnson'
  AND ep.HoursWorked > 150;


-- 2. Увеличить Budget всех проектов на 10%, если к ним назначен хотя бы один сотрудник из отдела 'IT'. 
UPDATE Projects
SET Budget = Budget * 1.10
WHERE ProjectID IN (
    SELECT DISTINCT ep.ProjectID
    FROM EmployeeProjects ep
    JOIN Employees e ON ep.EmployeeID = e.EmployeeID
    WHERE e.Department = 'IT'
);

-- 3. Для любого проекта, у которого еще нет EndDate (EndDate IS NULL), установить EndDate на один год позже его StartDate.
UPDATE Projects
SET EndDate = StartDate + INTERVAL '1 year'
WHERE EndDate IS NULL;


-- 4. Вставить нового сотрудника и немедленно назначить его на проект 'Website Redesign' с 80 отработанными часами, все в рамках одной транзакции. 
-- Использовать предложение RETURNING, чтобы получить EmployeeID вновь вставленного сотрудника.
BEGIN;

-- Вставляем нового сотрудника и используем RETURNING, чтобы динамически привязать его
WITH NewEmployee AS (
    INSERT INTO Employees (FirstName, LastName, Department, Salary)
    VALUES ('Grace', 'Hopper', 'IT', 85000.00)
    RETURNING EmployeeID
)
-- Назначаем его на 'Website Redesign' с 80 часами
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 
    ne.EmployeeID,
    p.ProjectID,
    80
FROM NewEmployee ne
CROSS JOIN Projects p
WHERE p.ProjectName = 'Website Redesign';

COMMIT;