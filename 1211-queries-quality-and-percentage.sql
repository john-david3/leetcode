-- # Write your MySQL query statement below
SELECT query_name, 
ROUND(AVG(rating/position),2) as quality,
ROUND((SELECT COUNT(Y.rating) FROM Queries as Y
WHERE Y.rating < 3 
AND Y.query_name = X.query_name) / COUNT(X.rating) * 100,2) as poor_query_percentage
FROM Queries as X
WHERE query_name IS NOT NULL
GROUP BY query_name
