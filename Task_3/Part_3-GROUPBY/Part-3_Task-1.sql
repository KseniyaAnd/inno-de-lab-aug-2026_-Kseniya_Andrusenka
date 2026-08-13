-- Подсчитайте количество клиентов в каждой стране. --

SELECT
  c.country,
  COUNT(c.country) AS count
FROM customers c
GROUP BY c.country
ORDER BY count DESC;