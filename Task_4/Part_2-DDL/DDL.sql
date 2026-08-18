-- 1. Создать новую таблицу с именем Departments
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);


-- 2. Изменить таблицу Employees, добавив новый столбец с именем Email (VARCHAR(100)). 
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);


-- 3. Заполнить столбец Email для всех текущих сотрудников уникальными значениями (например, через UPDATE).
UPDATE Employees
SET Email = LOWER(FirstName || '.' || LastName || '@company.com');


-- 4. Добавить ограничение UNIQUE к столбцу Email в таблице Employees.
ALTER TABLE Employees
ADD CONSTRAINT employees_email_unique UNIQUE (Email);


-- 5. Переименовать столбец Location в таблице Departments в OfficeLocation.
ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;