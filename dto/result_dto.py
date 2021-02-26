from dto.dto import DTO
from dto.student_dto import StudentDTO
from dto.topic_dto import TopicDTO


class ResultDTO(DTO):
    classes = {'student': StudentDTO,
               'topic': TopicDTO}

    def __init__(self, student=None, mark=None, date=None, topic=None, id=None):
        self.id = id
        self.student = student
        self.mark = mark
        self.date = date
        self.topic = topic

    @staticmethod
    def class_by_name(name):
        return ResultDTO.classes[name]

    def __str__(self):
        return f'student: {self.student} mark: {self.mark}\n date: {self.date} topic: {self.topic}'