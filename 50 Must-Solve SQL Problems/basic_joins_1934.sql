-- The confirmation rate of a user is the number of 'confirmed' messages 
-- divided by the total number of requested confirmation messages. 
-- The confirmation rate of a user that did not request any confirmation messages is 0. 
-- Round the confirmation rate to two decimal places.

SELECT 
    s.user_id,
    ROUND(AVG(IF(c.action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;

-- NULL VALUE is ignored in AVG, so we can use AVG instead of SUM/COUNT to calculate the confirmation rate.
-- SELECT 
--     s.user_id,
--     ROUND(
--         SUM(IF(c.action = 'confirmed', 1, 0)) / COUNT(c.action),
--         2
--     ) AS confirmation_rate
-- FROM Signups s
-- LEFT JOIN Confirmations c ON s.user_id = c.user_id
-- GROUP BY s.user_id;