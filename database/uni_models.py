import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped


Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Person():
    first_name = Column(String(250))
    last_name = Column(String(250))

class Student(Base, Person):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Group, backref="students")

subjects_to_teachers = Table('subjects_to_teachers', Base.metadata,
                             Column('id', Integer, primary_key=True),
                             Column('teacher_id', Integer, ForeignKey('teachers.id')),
                             Column('subject_id', Integer, ForeignKey('subjects.id'))
                             )
    
    
class Teacher(Base, Person):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    teachers: Mapped[list[Teacher]] = relationship(Teacher, backref="subjects", secondary=subjects_to_teachers)
    
    
class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(Student, backref='grades')
    
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship(Subject, backref='grades')
    