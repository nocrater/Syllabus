from service.service import CRUDService
from dto.teacher_dto import TeacherDTO
from repository.teacher_repository import TeacherRepository


class TeacherService(CRUDService):
    def __init__(self):
        super().__init__(TeacherDTO, TeacherRepository())