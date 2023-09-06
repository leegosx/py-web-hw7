from database.db_config import session, create_engine
from sqlalchemy import func, desc
from prettytable import PrettyTable
from database.uni_models import Student, Grade, Subject, Group, Teacher, subjects_to_teachers

def create_prettytable(*header, data):
    table = PrettyTable()
    table.field_names = header
    
    if data is not None:
        for item in data:
            table.add_row(item)
    return table

def create_prettytable_v2(field_name, data):
    table = PrettyTable()
    table.field_names = [field_name]

    for item in data:
        table.add_row([item])
    return table

def select_1():
    avg_grade = func.avg(Grade.grade).label("avg_grade")
    top_five_students = (
        session.query(Student.first_name, Student.last_name, func.round(avg_grade,2))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.first_name, Student.last_name)
        .order_by(avg_grade.desc())
        .limit(5)
        .all()
    )
    
    return create_prettytable('First name', 'Last name', 'GPA', data=top_five_students)

def select_2(subject_name):
    avg_grade = func.avg(Grade.grade).label("avg_grade")
    top_student = (
        session.query(Student.first_name, Student.last_name, func.round(avg_grade, 2))
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.first_name, Student.last_name)
        .order_by(avg_grade.desc())
        .limit(1)
        .first()
    )
    
    return create_prettytable("First name", "Last name", f"GPA in {subject_name}", data=[top_student])

def select_3(subject_name):
    avg_group_grade = func.avg(Grade.grade).label("avg_grade")
    
    avg_group_score = (
        session.query(Group.name, func.round(avg_group_grade, 2))
        .join(Student, Student.id == Grade.student_id)
        .join(Group, Student.group_id == Group.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.name)
        .order_by(avg_group_grade.desc())
        .all()
    )
    
    return create_prettytable("Group name", f"GPA in {subject_name}", data=avg_group_score)

def select_4():
    avg_score = func.avg(Grade.grade).label("avg_score")
    
    average_score = (
        session.query(func.round(avg_score, 2))
        .scalar()
        )
    
    return create_prettytable("Average score", data = [(average_score,)])

def select_5(teacher_first_name, teacher_last_name):
    courses = (
        session.query(Subject.name)
        .join(subjects_to_teachers, subjects_to_teachers.c.subject_id == Subject.id)
        .join(Teacher, subjects_to_teachers.c.teacher_id == Teacher.id)
        .filter(Teacher.first_name == teacher_first_name, Teacher.last_name == teacher_last_name)
        .all()
    )
    return create_prettytable_v2('Teachers subject', [course[0] for course in courses])

def select_6(group_name):
    students_in_group = (
        session.query(Student.first_name.concat(' ').concat(Student.last_name))
        .join(Group, Student.group_id == Group.id)
        .filter(Group.name == group_name)
        .all()
    )
    formatted_names = [" ".join(student) for student in students_in_group]
    return create_prettytable_v2("Students in Group", data=formatted_names)

def select_7(subject_name, group_name):
    student_grades = (
        session.query(Student.first_name, Student.last_name, Grade.grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .filter(Group.name == group_name)
        .all()
    )
    
    return create_prettytable("First name", "Last name", "Grade", data=student_grades)

def select_8(teacher_first_name, teacher_last_name):
    avg_score = func.avg(Grade.grade).label("avg_score")
    
    teacher_average_scores = (
        session.query(Subject.name, func.round(avg_score, 2))
        .join(subjects_to_teachers, subjects_to_teachers.c.subject_id == Subject.id)
        .join(Teacher, subjects_to_teachers.c.teacher_id == Teacher.id)
        .filter(Teacher.first_name == teacher_first_name, Teacher.last_name == teacher_last_name)
        .group_by(Subject.name)
        .all()
        
    )
    return create_prettytable('Subject', 'Average Score', data=teacher_average_scores)

def select_9(student_first_name, studnet_last_name):
    student_subjects =  (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .filter(Student.first_name == student_first_name, Student.last_name == studnet_last_name)
        .distinct()
        .all()
    )
    return create_prettytable('Subject', data=student_subjects)

def select_10(student_first_name, student_last_name, teacher_first_name, teacher_last_name):
    student_teacher_courses = (
        session.query(Subject.name)
            .join(Grade, Subject.id == Grade.subject_id)
            .join(Student, Grade.student_id == Student.id)
            .join(subjects_to_teachers, subjects_to_teachers.c.subject_id == Subject.id)  
            .join(Teacher, subjects_to_teachers.c.teacher_id == Teacher.id)
            .filter(Student.first_name == student_first_name, Student.last_name == student_last_name)
            .filter(Teacher.first_name == teacher_first_name, Teacher.last_name == teacher_last_name)
            .distinct()
            .all()
)
    return create_prettytable("Subject", data=student_teacher_courses)

def select_11(student_first_name, student_last_name, teacher_first_name, teacher_last_name):
    avg_teacher_student_score = (
        session.query(func.avg(Grade.grade).label("avg_score"))
        .join(Student, Grade.student_id == Student.id)
        .join(Subject, Grade.subject_id == Subject.id)
        .join(subjects_to_teachers, subjects_to_teachers.c.subject_id == Subject.id)
        .filter(Student.first_name == student_first_name, Student.last_name == student_last_name)
        .filter(Teacher.first_name == teacher_first_name, Teacher.last_name == teacher_last_name)
        .scalar()
    )
    
    return f"|||Average Score Given by {teacher_first_name} {teacher_last_name} to {student_first_name} {student_last_name}: {avg_teacher_student_score:.2f}|||"

def select_12(group_name, subject_name):
    last_lesson_grades = (
        session.query(Student.first_name, Student.last_name, Grade.grade)
        .join(Group, Student.group_id == Group.id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name)
        .filter(Subject.name == subject_name)
        .order_by(desc(Grade.date))
        .first()
    )
    
    return create_prettytable("First name", "Last name", "Grade", data=[last_lesson_grades])
if __name__ == "__main__":
    print(select_1())
    print(select_2('Sociology'))
    print(select_3('German'))
    print(select_4())
    print(select_5('Laura', 'Simpson'))
    print(select_6('107B'))
    print(select_7('Gender Studies', '120B'))
    print(select_8("Shelly", "Burke"))
    print(select_9('Kristin', 'Good'))
    print(select_10('Holly', 'Alexander', 'Laura', 'Simpson'))
    print(select_11('Holly', 'Alexander', 'Laura', 'Simpson'))
    print(select_12('107B', "German"))