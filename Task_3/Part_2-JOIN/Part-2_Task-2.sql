-- Выведите список доставок со статусом и именем клиента. --

SELECT
  s.status,
  c.first_name,
  c.last_name
FROM shippings s
INNER JOIN customers c 
  ON c.customer_id = s.customer;