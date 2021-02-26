from pony.orm import db_session

from model.teacher import Teacher
from repository.repository_imp import CRUDRepositoryImp

class TeacherRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Teacher)

    @staticmethod
    @db_session
    def from_dict(teacher):
        args = teacher
        return args

    @staticmethod
    def to_dict(teacher):
        d = teacher.to_dict()
        del d['classtype']
        return d