SELECT s.id, s.name, ROUND(AVG(g.grade)) as average_grade
FROM Students s
JOIN Grades g ON s.id = g.student_id
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 5
