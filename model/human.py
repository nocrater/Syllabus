from database import db, PrimaryKey, Required
from datetime import date


class Human(db.Entity):
    id = PrimaryKey(int, auto=True)
    first_name = Required(str)
    second_name = Required(str)
    patronymic = Required(str)
    date = Required(date)