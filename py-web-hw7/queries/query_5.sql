SELECT t.name AS teacher, s.name AS subject
FROM Subjects s
JOIN Teachers t ON s.teacher_id = t.id
WHERE t.name = 'Joseph Phillips';
