SELECT Subjects.name AS Subject
FROM Students
JOIN Grades ON Students.id = Grades.student_id
JOIN Subjects ON Grades.subject_id = Subjects.id
WHERE Students.name = "David Smith"
GROUP BY Subjects.name;


