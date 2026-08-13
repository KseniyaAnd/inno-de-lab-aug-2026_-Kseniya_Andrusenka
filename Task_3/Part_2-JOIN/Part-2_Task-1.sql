-- Получите список заказов вместе с именем клиента, который сделал заказ. --

SELECT
  c.first_name,
  c.last_name,
  o.item,
  o.amount
FROM orders o
INNER JOIN customers c 
  ON c.customer_id = o.customer_id;