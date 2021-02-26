from presenters.object_presenter import ObjectPresenter
from service.direction_service import DirectionService
from service.student_service import StudentService
from service.klas_service import KlasService
from service.syllabus_service import SyllabusService
from view.contracts import IKlasView


class KlasPresenter(ObjectPresenter):
    def __init__(self, view: IKlasView) -> None:
        ObjectPresenter.__init__(self, view, KlasService)
        self.directions = {i.name: i for i in DirectionService().get_all()}
        self.view.set_direction_items(self.directions.keys())
        self.syllabuses = {str(i): i for i in SyllabusService().get_all()}
        self.view.set_syllabus_items(self.syllabuses.keys())
        self.students = {i.name: i for i in StudentService().get_all()}
        self.view.set_student_items(self.students.keys())

    def to_view(self):
        self.view.set_date(self.object.date)
        self.view.set_letter(self.object.letter)
        if self.object.direction:
            self.view.set_direction(self.object.direction.full_name())
        if self.object.syllabus:
            self.view.set_syllabus(self.object.syllabus.full_name())
        if self.object.students:
            self.view.set_students([i.name for i in self.object.students])

    def from_view(self):
        self.object.date = self.view.get_date()
        self.object.letter = self.view.get_letter()
        self.object.direction = self.directions[self.view.get_direction()]
        self.object.syllabus = self.syllabuses[self.view.get_syllabus()]
        self.object.students = [self.students[i] for i in self.view.get_students()]
        

