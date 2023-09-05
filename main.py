from database.db_config import session
from seeds.seed import populate_teachers, populate_subjects, populate_students, populate_grades, populate_groups, populate_subjects_to_teachers

def main():
    populate_teachers()
    populate_subjects()
    populate_subjects_to_teachers()
    populate_groups()
    populate_students()
    populate_grades()
    session.commit()
    
if __name__ == "__main__":
    main()