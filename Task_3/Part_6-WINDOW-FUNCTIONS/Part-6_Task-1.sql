-- Для каждого заказа добавьте колонку с суммой всех заказов этого клиента (используя оконную функцию). --

SELECT
  o.order_id,
  o.customer_id,
  o.item,
  o.amount,
  SUM(o.amount) OVER (PARTITION BY o.customer_id) AS total_by_customer
FROM orders o;