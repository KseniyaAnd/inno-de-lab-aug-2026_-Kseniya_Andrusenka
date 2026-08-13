-- Найдите клиентов, которые: 
--   1. Сделали хотя бы 2 заказа (любых), 
--   2. Имеют хотя бы одну доставку со статусом 'Delivered'. 
-- Для каждого такого клиента выведите: 
--   ● full_name (имя + фамилия), 
--   ● общее количество заказов, 
--   ● общую сумму заказов, 
--   ● страну проживания. 

SELECT
  c.first_name || ' ' || c.last_name AS full_name,
  c.country,
  SUM(o.amount) AS total_orders,
  COUNT(o.item) AS item_count
FROM orders o
INNER JOIN customers c 
  ON c.customer_id = o.customer_id 
INNER JOIN shippings s 
  ON s.shipping_id = c.customer_id  
WHERE s.status = 'Delivered'
  AND c.customer_id IN (
    SELECT customer_id 
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(item) > 1
  )
GROUP BY
  c.customer_id,
  c.first_name,
  c.last_name,
  c.country;