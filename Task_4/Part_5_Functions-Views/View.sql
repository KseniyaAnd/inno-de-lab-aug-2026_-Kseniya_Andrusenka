-- 3. Создание представления IT_Department_View для сотрудников из отдела 'IT'
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Salary
FROM Employees
WHERE Department = 'IT';


-- 4. Выборка данных из созданного представления
SELECT * FROM IT_Department_View;