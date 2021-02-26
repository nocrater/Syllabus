from model.human import Human
from repository.repository_imp import CRUDRepositoryImp


class HumanRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Human)

    @staticmethod
    def to_dict(human):
        d = human.to_dict()
        if 'klas' in d:
            del d['klas']
        del d['classtype']
        return d