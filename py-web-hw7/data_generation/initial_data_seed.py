from models import Student, Group, Teacher, Subject, Grade, session
from fake_subject_and_group import fake_group_name, fake_subject
from faker import Faker

fake = Faker()

def populate_teachers(num_teachers=5):
    for _ in range(num_teachers):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        session.add(teacher)
        
def populate_subjects(num_groups=8):
    for _ in range(num_groups):
        subject = Subject(
            name = fake_subject()
        )
        
    session.add(subject)
    
def populate_students(num_students=50):
    for _ in range(num_students):
        group = Group.query.filter(Group.name == fake_group_name()).first()
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group=group
        )
        session.add(student)
  
def populate_group(num_groups=3):
    for _ in range(num_groups):
        group = Group(
            group_name = fake_group_name()
        )
        
        session.add(group)
        
