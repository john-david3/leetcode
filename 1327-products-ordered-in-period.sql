-- # Write your MySQL query statement below
SELECT p.product_name, SUM(unit) as unit
FROM Products as p JOIN Orders as o
ON p.product_id = o.product_id
WHERE o.order_date LIKE '2020-02-%'
GROUP BY product_name
HAVING SUM(unit) >= 100

