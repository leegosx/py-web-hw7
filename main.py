from models.uni_models import session, Base, engine
from data_generation.initial_data_seed import populate_teachers, populate_subjects, populate_students, populate_grades, populate_groups, populate_subjects_to_teachers

def main():
    populate_teachers()
    populate_subjects()
    populate_subjects_to_teachers()
    populate_students()
    populate_grades()
    populate_groups()
    Base.metadata.create_all(engine) 
    session.commit()
    
if __name__ == "__main__":
    main()