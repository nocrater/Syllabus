from pony.orm import db_session

from model.studying import Studying
from model.syllabus import Syllabus
from repository.repository_imp import CRUDRepositoryImp


class SyllabusRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Syllabus)

    @staticmethod
    @db_session
    def from_dict(syllabus):
        args = syllabus
        args['studyings'] = set(map(lambda arg: Studying.get(id=arg['id']), args['studyings']))
        return args

    @staticmethod
    def to_dict(syllabus):
        d = syllabus.to_dict(with_collections=True)
        d['studyings'] = list(map(lambda item: {'id': item}, d['studyings']))
        if 'klas' in d:
            del d['klas']
        return d

    @db_session
    def all(self, **attrs):
        return self.to_collection_dict(self.klass.select(**attrs).prefetch(Studying)[:])