from models.uni_models import session
from data_generation.initial_data_seed import populate_teachers, populate_subjects, populate_students, populate_grades, populate_groups

def main():
    populate_teachers()
    populate_subjects()
    populate_students()
    populate_grades()
    populate_groups() 
    session.commit()
    
if __name__ == "__main__":
    main()