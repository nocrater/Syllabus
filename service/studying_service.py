from service.service import CRUDService
from dto.studying_dto import StudyingDTO
from dto.subject_dto import SubjectDTO
from repository.studying_repository import StudyingRepository
from repository.subject_repository import SubjectRepository

class StudyingService(CRUDService):
    def __init__(self):
        super().__init__(StudyingDTO, StudyingRepository())
        self.subject_repository = SubjectRepository()

    def load_subjects(self, studying):
        if studying.subjects:
            studying.subjects = list(
                map(lambda item: SubjectDTO.from_dict(self.subject_repository.find(item.id)), studying.subjects))