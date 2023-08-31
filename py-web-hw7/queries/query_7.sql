SELECT s.name, g.grade
FROM Students s
JOIN Grades g ON s.id = g.student_id
WHERE s.group_id = 3 AND g.subject_id = 4;
