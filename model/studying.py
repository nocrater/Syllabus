from database import db, PrimaryKey, Required, Optional, Set
from model.subject import Subject
from datetime import time, date


class Studying(db.Entity):
    id = PrimaryKey(int, auto=True)
    beginning_time = Required(time)
    date = Required(date)
    klas = Optional('Klas')
    syllabus = Optional('Syllabus')
    subjects = Set(Subject)
