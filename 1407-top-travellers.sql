-- # Write your MySQL query statement below
SELECT u.name, COALESCE(SUM(r.distance), 0) as travelled_distance
FROM Users as u LEFT JOIN Rides as r
ON u.id = r.user_id
GROUP BY user_id
ORDER BY SUM(r.distance) DESC, u.name