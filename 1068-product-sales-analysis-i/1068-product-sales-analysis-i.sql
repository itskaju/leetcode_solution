# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales as s1
LEFT JOIN Product as p1
ON s1.product_id = p1.product_id
