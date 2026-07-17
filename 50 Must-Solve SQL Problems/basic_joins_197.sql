--Write a solution to find all dates id with higher temperatures 
--compared to its previous dates (yesterday).

SELECT a.id
FROM Weather AS a
JOIN Weather AS b
    ON a.recordDate = DATE_ADD(b.recordDate, INTERVAL 1 DAY) --MySQL
WHERE a.temperature > b.temperature;