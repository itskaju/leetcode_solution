# Write your MySQL query statement below
SELECT d.name AS Department ,
       e1.name AS Employee,
       e1.salary AS salary
FROM Employee e1 INNER JOIN Department d
ON e1.departmentID = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT (e2.salary))
    FROM Employee e2
    WHERE e2.salary > e1.salary AND
    e1.DepartmentID = e2.DepartmentID
)
