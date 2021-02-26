from pony.orm import db_session

from model.klas import Klas
from model.direction import Direction
from model.syllabus import Syllabus
from model.studying import Studying
from model.student import Student

from repository.repository_imp import CRUDRepositoryImp


class KlasRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Klas)

    @staticmethod
    @db_session
    def from_dict(klas):
        args = klas
        args['direction'] = Direction.get(id=args['direction']['id'])
        args['syllabus'] = Syllabus.get(id=args['syllabus']['id'])
        args['students'] = set(map(lambda arg: Student.get(id=arg['id']), args['students']))
        return args

    @staticmethod
    def to_dict(klas):
        d = klas.to_dict(with_collections=True)
        d['direction'] = {'id': d['direction']}
        d['syllabus'] = {'id': d['syllabus']}
        d['students'] = list(map(lambda item: {'id': item}, d['students']))
        return d

    @db_session
    def all(self, **attrs):
        return self.to_collection_dict(self.klass.select(**attrs).prefetch(Direction, Syllabus, Student)[:])