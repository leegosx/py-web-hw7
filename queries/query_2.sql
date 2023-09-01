SELECT s.id, s.name, AVG(g.grade) as average_grade
FROM Students s
JOIN Grades g ON s.id = g.student_id
WHERE g.subject_id = 7
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 1
