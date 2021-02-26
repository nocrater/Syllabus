from pony.orm import db_session

from model.studying import Studying
from model.subject import Subject
from repository.repository_imp import CRUDRepositoryImp


class StudyingRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Studying)

    @staticmethod
    @db_session
    def from_dict(old):
        args = old
        args['subjects'] = set(map(lambda arg: Subject.get(id=arg['id']), args['subjects']))
        return args

    @staticmethod
    def to_dict(studying):
        d = studying.to_dict(with_collections=True)
        d['subjects'] = list(map(lambda item: {'id': item}, d['subjects']))
        if 'klas' in d:
            del d['klas']
        return d

    @db_session
    def all(self, **attrs):
        return self.to_collection_dict(self.klass.select(**attrs).prefetch(Subject)[:])