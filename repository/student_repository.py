from pony.orm import db_session

from model.student import Student
from repository.repository_imp import CRUDRepositoryImp


class StudentRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Student)

    @staticmethod
    @db_session
    def from_dict(student):
        args = student
        return args

    @staticmethod
    def to_dict(student):
        d = student.to_dict()
        del d['classtype']
        return d