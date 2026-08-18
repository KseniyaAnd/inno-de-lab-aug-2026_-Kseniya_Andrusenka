-- Предоставление прав INSERT и UPDATE администратором
-- Возвращаемся в сессию администратора и выдаем права
GRANT INSERT, UPDATE ON Employees TO hr_user;

-- Так как поле EmployeeID является SERIAL (использует последовательность),
-- пользователю также необходимо дать право USAGE на последовательность для работы INSERT:
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;