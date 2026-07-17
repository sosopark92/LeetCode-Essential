SELECT p.project_id, round(avg(e.experience_years),2) AS average_years FROM project AS p
LEFT JOIN employee AS e
ON e.employee_id = p.employee_id
GROUP BY p.project_id
ORDER BY p.project_id;
