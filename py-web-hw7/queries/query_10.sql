SELECT st.name AS Student, Subjects.name AS Subject
FROM Students AS st
JOIN Grades AS g ON st.id = g.student_id
JOIN Subjects AS Subjects ON g.subject_id = Subjects.id
JOIN Teachers AS t ON Subjects.teacher_id = t.id
WHERE st.name = 'Jeremy Garcia' 
  AND t.name = 'Katherine Griffin'
GROUP BY Subjects.name;

