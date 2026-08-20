-- Data Warehouse: "Онлайн-магазин электроники"
-- Бизнес-процесс: Продажи (заказы)
-- Схема: Star Schema
-- Гранулярность: одна строка факта = одна позиция товара в заказе

-- ---------- ИЗМЕРЕНИЯ ----------

CREATE TABLE dim_date (
    date_key    INT PRIMARY KEY,   
    full_date   DATE NOT NULL,
    month       SMALLINT NOT NULL,
    quarter     SMALLINT NOT NULL,
    year        SMALLINT NOT NULL
);

CREATE TABLE dim_customer (
    customer_key  INT PRIMARY KEY,
    customer_id   INT NOT NULL,     
    full_name     VARCHAR(200) NOT NULL,
    email         VARCHAR(255) NOT NULL
);

CREATE TABLE dim_product (
    product_key    INT PRIMARY KEY,
    product_id     INT NOT NULL,    
    product_name   VARCHAR(255) NOT NULL,
    category_name  VARCHAR(100) NOT NULL,
    price          NUMERIC(10, 2) NOT NULL
);

-- ---------- ФАКТ ----------

CREATE TABLE fact_sales (
    sale_key       BIGINT PRIMARY KEY,
    date_key       INT NOT NULL REFERENCES dim_date(date_key),
    customer_key   INT NOT NULL REFERENCES dim_customer(customer_key),
    product_key    INT NOT NULL REFERENCES dim_product(product_key),
    order_id       INT NOT NULL,         
    quantity       INT NOT NULL,         
    unit_price     NUMERIC(10, 2) NOT NULL,
    total_amount   NUMERIC(10, 2) NOT NULL  
);

-- Запрос 1. Выручка по категориям товаров.
-- Вопрос: какие категории приносят больше всего денег?
SELECT p.category_name,
       SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.category_name
ORDER BY revenue DESC;


-- Запрос 2. ТОП-5 товаров по выручке.
-- Вопрос: какие товары продаются лучше всего?
SELECT p.product_name,
       SUM(f.quantity) AS units_sold,
       SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 5;


-- Запрос 3. Выручка по месяцам.
-- Вопрос: как меняются продажи со временем?
SELECT d.year, d.month,
       SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

