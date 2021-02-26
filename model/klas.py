from database import db, PrimaryKey, Required, Optional, Set
from model.student import Student
from model.direction import Direction
from model.studying import Studying
from model.syllabus import Syllabus
from datetime import datetime


class Klas(db.Entity):
    id = PrimaryKey(int, auto=True)
    date = Required(datetime)
    number = Required(int)
    letter = Required(str)
    direction = Required(Direction)
    syllabus = Required(Syllabus)
    studying = Optional(Studying)
    students = Set(Student)


