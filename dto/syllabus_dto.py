from dto.dto import DTO
from dto.studying_dto import StudyingDTO


class SyllabusDTO(DTO):
    classes = {'studyings': StudyingDTO}

    def __init__(self, start=None, finish=None, studyings=None, id=None):
        self.id = id
        self.start = start
        self.finish = finish
        self.studyings = studyings

    @staticmethod
    def class_by_name(name):
        return SyllabusDTO.classes[name]

    def __str__(self):
        return f'Начало: {self.start} Конец: {self.finish}'