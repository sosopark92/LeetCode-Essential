-- Write a solution to report the movies with an odd-numbered ID 
-- and a description that is not "boring".
-- ordered by rating in descending order.

SELECT * FROM cinema
WHERE id % 2 = 1 AND DESCRIPTION <> 'boring'
ORDER BY rating DESC;