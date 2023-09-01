SELECT Teachers.name AS Teacher, Subjects.name AS Subject, ROUND(AVG(Grades.grade)) AS Average_Grade
FROM Grades
JOIN Students ON Grades.student_id = Students.id
JOIN Subjects ON Grades.subject_id = Subjects.id
JOIN Teachers ON Subjects.teacher_id = Teachers.id
WHERE Teachers.id = 4
GROUP BY Subjects.id;