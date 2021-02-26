from database import db, PrimaryKey, Required, Optional, Set
from model.studying import Studying
from datetime import date


class Syllabus(db.Entity):
    id = PrimaryKey(int, auto=True)
    klas = Optional('Klas')
    start = Required(date)
    finish = Required(date)
    studyings = Set(Studying)