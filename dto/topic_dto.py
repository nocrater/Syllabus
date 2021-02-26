from dto.dto import DTO
from dto.subject_dto import SubjectDTO


class TopicDTO(DTO):
    classes = {'subjects': SubjectDTO}

    def __init__(self, name=None, subjects=None, results=None, id=None):
        self.id = id
        self.name = name
        self.subjects = subjects

    @staticmethod
    def class_by_name(name):
        return TopicDTO.classes[name]

    def __str__(self):
        return f'name: {self.name} subjects: {", ".join([str(i) for i in self.subjects])}'
