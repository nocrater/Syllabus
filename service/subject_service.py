from service.service import CRUDService
from dto.subject_dto import SubjectDTO
from repository.subject_repository import SubjectRepository
from repository.teacher_repository import TeacherRepository
from dto.teacher_dto import TeacherDTO


class SubjectService(CRUDService):
    def __init__(self):
        super().__init__(SubjectDTO, SubjectRepository())
        self.teacher_repository = TeacherRepository()

    def load_teacher(self, emp):
        emp.teacher = TeacherDTO.from_dict(self.teacher_repository.find(emp.teacher.id))
