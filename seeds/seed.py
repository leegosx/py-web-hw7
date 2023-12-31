from database.uni_models import Student, Group, Teacher, Subject, Grade
from database.db_config import session
from fake_subject_and_group.subject_group import fake_subject, fake_group_name
from faker import Faker

import random

fake = Faker()

def populate_teachers(num_teachers=5):
    for _ in range(num_teachers):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        session.add(teacher)
    session.commit()
        
def populate_subjects(num_subjects=8):
    for _ in range(num_subjects):
        subject = Subject(name = fake_subject())
        
        session.add(subject)
    session.commit()
        
def populate_subjects_to_teachers():
    try:
        all_teachers = session.query(Teacher).all()
        all_subjects = session.query(Subject).all()
        
        for teacher in all_teachers:
            subjects_for_teacher = random.sample(all_subjects, random.randint(1, 3))
            for subject in subjects_for_teacher:
                teacher.subjects.append(subject)
        
        session.commit()
        
    except Exception as e:
        print(f"Error populating subjects_to_teachers: {e}")
        session.rollback()
    finally:
        session.close()
        
def populate_students(num_students=50):
    groups = session.query(Group).all()
    if not groups:
        raise ValueError("No groups available. Please populate groups first.")
    
    for _ in range(num_students):
        group = random.choice(groups)
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group_id=group.id
        )
        session.add(student)
    session.commit()
    
def populate_groups(num_groups=3):
    for _ in range(num_groups):
        group = Group(name = fake_group_name())
        
        session.add(group)
    session.commit()
        
def populate_grades(num_grades=20):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students: 
        for _ in range(num_grades):
            grade_value = random.randint(1, 5)
            grade = Grade(
                grade = grade_value, 
                date = fake.date_this_year(), 
                student_id = student.id,
                subject_id = random.choice(subjects).id
            )
        
        session.add(grade)
    session.commit()