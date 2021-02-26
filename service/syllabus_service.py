from service.service import CRUDService
from dto.syllabus_dto import SyllabusDTO
from dto.studying_dto import StudyingDTO
from repository.syllabus_repository import SyllabusRepository
from repository.studying_repository import StudyingRepository

class SyllabusService(CRUDService):
    def __init__(self):
        super().__init__(SyllabusDTO, SyllabusRepository())
        self.studying_repository = StudyingRepository()

    def load_studyings(self, topic):
        if topic.studyings:
            topic.studyings = list(
                map(lambda item: StudyingDTO.from_dict(self.studying_repository.find(item.id)), topic.studyings))