from dto.dto import DTO
from dto.direction_dto import DirectionDTO
from dto.syllabus_dto import SyllabusDTO
from dto.student_dto import StudentDTO
from datetime import datetime


class KlasDTO(DTO):
    classes = {'direction': DirectionDTO,
               'syllabus': SyllabusDTO,
               'students': StudentDTO}

    def __init__(self, date=None, letter=None, direction=None, syllabus=None, studying=None, students=None, id=None):
        self.id = id
        self.date = date
        if date:
            self.number = self.get_number_today(date)
        self.letter = letter
        self.direction = direction
        self.syllabus = syllabus
        self.students = students

    def get_number_today(self, date):
        today = datetime.today()
        # +1, так как отсчет с единицы
        number = today.year - date.year + 1

        # до 1 июня класс еще не закончен и новый не наступает
        if today.month < 6:
            number = number-1
        return number

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    @staticmethod
    def class_by_name(name):
        return KlasDTO.classes[name]

    def __str__(self):
        return f'Дата набора: {self.date}\nНаправление: {self.direction} буква: {self.letter}' \
               f'\nУчебный план: {self.syllabus}\nУченики: {", ".join([str(i) for i in self.students])}'