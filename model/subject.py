from database import db, PrimaryKey, Required, Optional
from model.teacher import Teacher


class Subject(db.Entity):
    id = PrimaryKey(int, auto=True)
    topic = Optional('Topic', reverse='subjects')
    name = Required(str)
    teacher = Required(Teacher)
    schedule = Optional('Studying', reverse='subjects')