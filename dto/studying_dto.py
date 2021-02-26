from dto.dto import DTO
from dto.subject_dto import SubjectDTO


class StudyingDTO(DTO):
    classes = {'subjects': SubjectDTO}

    def __init__(self, beginning_time=None, date=None, syllabus=None, subjects=None,id=None):
        self.id = id
        self.beginning_time = beginning_time
        self.date = date
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        self.subjects.remove(subject)

    @staticmethod
    def class_by_name(name):
        return StudyingDTO.classes[name]

    def __str__(self):
        return f'\nbeginning_time: {self.beginning_time}\nТемы:{", ".join([str(i) for i in self.subjects])}'

    def title(self):
        return f'Уроки с {self.beginning_time} за {self.date}'