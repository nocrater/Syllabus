from database import db, PrimaryKey, Required, Set
from model.subject import Subject


class Topic(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    subjects = Set(Subject)
    results = Set('Result')
