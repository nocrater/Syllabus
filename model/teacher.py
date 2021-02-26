from database import db, Set
from model.human import Human


class Teacher(Human):
    subjects = Set('Subject')