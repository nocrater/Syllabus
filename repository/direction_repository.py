from pony.orm import db_session

from model.direction import Direction
from repository.repository_imp import CRUDRepositoryImp

class DirectionRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Direction)

    @staticmethod
    @db_session
    def from_dict(direction):
        args = direction
        return args

    @staticmethod
    def to_dict(direction):
        d = direction.to_dict()
        if 'klas' in d:
            del d['klas']
        return d
