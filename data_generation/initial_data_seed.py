from models.uni_models import Student, Group, Teacher, Subject, Grade, session
from fake_subject_and_group import fake_group_name, fake_subject
from faker import Faker
from random import choice, randint

fake = Faker()

def populate_teachers(num_teachers=5):
    for _ in range(num_teachers):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

    session.add(teacher)
    session.commit()
        
def populate_subjects(num_groups=8):
    for _ in range(num_groups):
        subject = Subject(
            name = fake_subject()
        )
        
    session.add(subject)
    session.commit()
    
def populate_students(num_students=50):
    for _ in range(num_students):
        group = Group.query.filter(Group.name == fake_group_name()).first()
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group=group
        )
    session.add(student)
    session.commit()
    
def populate_groups(num_groups=3):
    for _ in range(num_groups):
        group = Group(group_name = fake_group_name())
        
    session.add(group)
    session.commit()
        
def populate_grades(num_grades=20):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for student in students: 
        for _ in range(num_grades):
            grade_value = randint(1, 5)
            grade = Grade(
                grade = grade_value, 
                date = fake.date_this_year(), 
                student_id = student.id,
                subject_id = choice(subjects).id
            )
        
    session.add(grade)
    session.commit()