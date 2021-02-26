from pony.orm import db_session

from model.subject import Subject
from model.teacher import Teacher
from repository.repository_imp import CRUDRepositoryImp


class SubjectRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Subject)

    @staticmethod
    @db_session
    def from_dict(subject):
        args = subject
        args['teacher'] = Teacher.get(id=args['teacher']['id'])
        return args

    @staticmethod
    def to_dict(subject):
        d = subject.to_dict()
        d['teacher'] = {'id': d['teacher']}
        return d
