-- # Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z]{1}[A-Za-z0-9_.-]*@leetcode\\.com$'