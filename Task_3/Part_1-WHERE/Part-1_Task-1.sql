-- Найдите всех клиентов из страны 'USA', которым больше 25 лет. --

SELECT *
FROM customers c
WHERE c.country = 'USA'
  AND c.age > 25;