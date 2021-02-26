from database import db, PrimaryKey, Required
from model.student import Student
from datetime import date


class Result(db.Entity):
    id = PrimaryKey(int, auto=True)
    student = Required(Student)
    topic = Required('Topic')
    mark = Required(int)
    date = Required(date)
