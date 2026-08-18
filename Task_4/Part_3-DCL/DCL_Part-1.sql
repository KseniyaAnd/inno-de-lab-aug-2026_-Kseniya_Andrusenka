-- 1.  Создать нового пользователя PostgreSQL (роль) с именем hr_user и паролем. 
CREATE ROLE hr_user WITH LOGIN PASSWORD 'hr_password';


-- 2. Предоставить hr_user право SELECT на таблицу Employees.
GRANT SELECT ON TABLE Employees TO hr_user;