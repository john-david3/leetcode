-- Write your MySQL query statement below
SELECT w1.id
FROM Weather as w1 JOIN Weather as w2
WHERE DATEDIFF(w1.recordDate, w2.recordDate) BETWEEN 1 AND 1
AND w1.temperature > w2.temperature;