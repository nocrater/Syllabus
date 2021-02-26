from service.service import CRUDService
from dto.klas_dto import KlasDTO
from dto.direction_dto import DirectionDTO
from dto.student_dto import StudentDTO
from dto.syllabus_dto import SyllabusDTO
from repository.klas_repository import KlasRepository
from repository.direction_repository import DirectionRepository
from repository.student_repository import StudentRepository
from repository.syllabus_repository import SyllabusRepository


class KlasService(CRUDService):
    def __init__(self):
        super().__init__(KlasDTO, KlasRepository())
        self.direction_repository = DirectionRepository()
        self.syllabus_repository = SyllabusRepository()
        self.student_repository = StudentRepository()

    def load_direction(self, emp):
        emp.direction = DirectionDTO.from_dict(self.direction_repository.find(emp.direction.id))

    def load_syllabus(self, emp):
        emp.syllabus = SyllabusDTO.from_dict(self.syllabus_repository.find(emp.syllabus.id))

    def load_students(self, klas):
        if klas.students:
            klas.students = list(
                map(lambda item: StudentDTO.from_dict(self.student_repository.find(item.id)), studying.students))