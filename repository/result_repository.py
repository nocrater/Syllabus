from pony.orm import db_session

from model.result import Result
from model.student import Student
from model.topic import Topic
from repository.repository_imp import CRUDRepositoryImp


class ResultRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Result)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['student'] = Student.get(id=args['student']['id'])
        args['topic'] = Topic.get(id=args['topic']['id'])
        return args

    @staticmethod
    def to_dict(result):
        d = result.to_dict()
        d['student'] = {'id': d['student']}
        d['topic'] = {'id': d['topic']}
        return d
