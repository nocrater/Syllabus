from service.service import CRUDService
from dto.topic_dto import TopicDTO
from dto.subject_dto import SubjectDTO
from repository.subject_repository import SubjectRepository
from repository.topic_repository import TopicRepository


class TopicService(CRUDService):
    def __init__(self):
        super().__init__(TopicDTO, TopicRepository())
        self.subject_repository = SubjectRepository()

    def load_subjects(self, topic):
        if topic.subjects:
            topic.subjects = list(
                map(lambda item: SubjectDTO.from_dict(self.subject_repository.find(item.id)), topic.subjects))
