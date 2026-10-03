# Write your MySQL query statement below
SELECT v1.customer_id , COUNT(customer_id) AS count_no_trans
FROM Visits as v1
LEFT JOIN Transactions as t1
ON v1.visit_id = t1.visit_id
WHERE  transaction_id is NULL
GROUP BY v1.customer_id