from dto.dto import DTO
from dto.teacher_dto import TeacherDTO


class SubjectDTO(DTO):
    classes = {'teacher': TeacherDTO}

    def __init__(self, name=None, teacher=None, topic=None, schedule=None, id=None):
        self.id = id
        self.name = name
        self.teacher = teacher

    @staticmethod
    def class_by_name(name):
        return SubjectDTO.classes[name]

    def __str__(self):
        return f'name: {self.name}'
