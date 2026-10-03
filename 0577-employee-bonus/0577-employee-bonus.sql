# Write your MySQL query statement below
SELECT name, bonus
FROM Employee  as e1
LEFT JOIN Bonus as b1
ON e1.empID = b1.empID
WHERE  b1.bonus is NULL OR b1.bonus < 1000