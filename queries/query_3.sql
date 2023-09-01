SELECT gr.name, ROUND(AVG(g.grade)) AS average_score
FROM Groups gr
JOIN Students s ON gr.id = s.group_id
JOIN Grades g ON s.id = g.student_id
JOIN Subjects sj ON g.subject_id = sj.id
WHERE g.subject_id = 2
GROUP BY gr.id;
