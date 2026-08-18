-- 1. Создание функции CalculateAnnualBonus для расчёта бонуса (10% от зарплаты)
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    p_employee_id INT,
    p_salary DECIMAL(10, 2)
)
RETURNS DECIMAL(10, 2) 
LANGUAGE plpgsql
AS $$
BEGIN
    -- Возвращаем 10% от переданного значения зарплаты
    RETURN p_salary * 0.10;
END;
$$;


-- 2. Использование функции в SELECT для расчета бонуса всех сотрудников
SELECT 
    EmployeeID,
    FirstName,
    LastName,
    Department,
    Salary,
    CalculateAnnualBonus(EmployeeID, Salary) AS PotentialBonus
FROM Employees;