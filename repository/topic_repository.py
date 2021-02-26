from pony.orm import db_session

from model.topic import Topic
from model.subject import Subject
from model.result import Result

from repository.repository_imp import CRUDRepositoryImp


class TopicRepository(CRUDRepositoryImp):
    def __init__(self):
        super().__init__(Topic)

    @staticmethod
    @db_session
    def from_dict(topic):
        args = topic
        args['subjects'] = set(map(lambda arg: Subject.get(id=arg['id']), args['subjects']))
        return args

    @staticmethod
    def to_dict(topic):
        d = topic.to_dict(with_collections=True)
        d['subjects'] = list(map(lambda item: {'id': item}, d['subjects']))
        if 'results' in d:
            del d['results']
        return d

    @db_session
    def all(self, **attrs):
        return self.to_collection_dict(self.klass.select(**attrs).prefetch(Subject)[:])