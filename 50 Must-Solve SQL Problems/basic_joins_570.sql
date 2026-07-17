SELECT e2.name FROM employee AS e1
JOIN employee AS e2
    ON e1.managerId = e2.id
GROUP BY e1.managerId, e2.name
HAVING COUNT(*) >= 5