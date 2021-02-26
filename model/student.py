from pony.orm import Optional, Set
from model.human import Human


class Student(Human):
    klas = Optional('Klas')
    results = Set('Result')