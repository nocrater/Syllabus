from dto.direction_dto import DirectionDTO
from dto.human_dto import HumanDTO
from dto.klas_dto import KlasDTO
from dto.result_dto import ResultDTO
from dto.student_dto import StudentDTO
from dto.studying_dto import StudyingDTO
from dto.subject_dto import SubjectDTO
from dto.syllabus_dto import SyllabusDTO
from dto.teacher_dto import TeacherDTO
from dto.topic_dto import TopicDTO

from service.direction_service import DirectionService
from service.human_service import HumanService
from service.klas_service import KlasService
from service.result_service import ResultService
from service.student_service import StudentService
from service.studying_service import StudyingService
from service.subject_service import SubjectService
from service.syllabus_service import SyllabusService
from service.teacher_service import TeacherService
from service.topic_service import TopicService

from binding import *

from datetime import datetime

human1 = HumanDTO(first_name="Василий", second_name="Гы", patronymic="Вжыч", date=datetime(2000, 1, 12))
human2 = HumanDTO(first_name="Дол", second_name="Гаы", patronymic="Ан", date=datetime(2001, 2, 12))

human_service = HumanService()

print('\nЛюди:\n')

human_service.create(human1)
print(human1)

human_service.create(human2)
print(human2)

# Update name
human1.first_name = "Дарья"
human_service.update(human1)
print(human1)

# Get all humans
for human in human_service.get_all():
    print(human.first_name)

direction = DirectionDTO(name='Физмат')

direction_service = DirectionService()

print('\nНаправление:\n')

direction_service.create(direction)
print(direction)

syllabus = SyllabusDTO(start=2019, finish=2020)

syllabus_service = SyllabusService()

print('\nПлан:\n')

syllabus_service.create(syllabus)
print(syllabus)

studying = StudyingDTO(beginning_time=datetime(2020, 9, 4, 9, 40, 0))

studying_service = StudyingService()

print('\nИзучение:\n')

studying_service.create(studying)
print(studying)

student1 = StudentDTO("Авав", "Авовов", "Арович", date=datetime(2000, 1, 12))
student2 = StudentDTO("Гав", "Вов", "Ович", date=datetime(2000, 4, 12))
student3 = StudentDTO("Мав", "Авв", "Жим", date=datetime(2000, 5, 12))

student_service = StudentService()

student_service.create(student1)
student_service.create(student2)
student_service.create(student3)

print('\nУченики:\n')

all_students = student_service.get_all()
for student in all_students:
    print(student)

klass = KlasDTO(date=datetime(2013, 9, 1), letter="a", direction=direction, syllabus=syllabus, studying=studying, students=all_students)

klas_service = KlasService()

print('\nКласс:\n')

klas_service.create(klass)
print(klass)

teacher = TeacherDTO("Учитель", "Учителев", "Утичелевич", date=datetime(1950, 1, 12))
teacher2 = TeacherDTO("Учитель2", "Учителев2", "Утичелевич2", date=datetime(1952, 1, 12))

teacher_service = TeacherService()

teacher_service.create(teacher)
teacher_service.create(teacher2)

print('\nУчитель:\n')

all_teachers = teacher_service.get_all()
for teacher in all_teachers:
    print(teacher)

subject1 = SubjectDTO("Физика. Оптика", teacher)
subject2 = SubjectDTO("Физика. Механика", teacher)

subject_service = SubjectService()

subject_service.create(subject1)
subject_service.create(subject2)

print('\nТемы:\n')

all_subjects = subject_service.get_all()
for subject in all_subjects:
    print(subject)

topic = TopicDTO(name="Физика", subjects=all_subjects, results=[])

topic_service = TopicService()

print('\nПредмет:\n')

topic_service.create(topic)
print(topic)

result = ResultDTO(student=student1, topic=topic, mark=5, date=datetime(2020, 9, 4))

result_service = ResultService()

print('\nРезультат:\n')

result_service.create(result)
print(result)
