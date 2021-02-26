from service.service import CRUDService
from dto.result_dto import ResultDTO
from dto.student_dto import StudentDTO
from repository.result_repository import ResultRepository
from repository.student_repository import StudentRepository


class ResultService(CRUDService):
    def __init__(self):
        super().__init__(ResultDTO, ResultRepository())
        self.student_repository = StudentRepository()

    def load_student(self, emp):
        emp.student = StudentDTO.from_dict(self.student_repository.find(emp.student.id))

    def load_topic(self, emp):
        emp.topic = StudentDTO.from_dict(self.topic_repository.find(emp.topic.id))
