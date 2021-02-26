from service.service import CRUDService
from dto.student_dto import StudentDTO
from repository.student_repository import StudentRepository


class StudentService(CRUDService):
    def __init__(self):
        super().__init__(StudentDTO, StudentRepository())