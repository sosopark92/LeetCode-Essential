SELECT
    p.product_id,
    IFNULL(
        ROUND(SUM(p.price * u.units) /   SUM(u.units), 2),
        0
    ) AS average_price 
FROM Prices p
LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

-- IFNULL to handle cases where there are no units sold for a product, resulting in NULL average price. 
-- SUM() ignores NULL when at least one numeric value exists, 
-- but when all values are NULL, the result is NULL, not 0.