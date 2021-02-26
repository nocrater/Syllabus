from presenters.object_presenter import ObjectPresenter
from service.subject_service import SubjectService
from service.teacher_service import TeacherService
from view.contracts import ISubjectView


class SubjectPresenter(ObjectPresenter):
    def __init__(self, view: ISubjectView) -> None:
        ObjectPresenter.__init__(self, view, SubjectService)
        self.teachers = {i.full_name(): i for i in TeacherService().get_all()}
        self.view.set_teacher_items(self.teachers.keys())

    def to_view(self):
        self.view.set_name(self.object.name)
        if self.object.teacher:
            self.view.set_teacher(self.object.teacher.full_name())

    def from_view(self):
        self.object.name = self.view.get_name()
        self.object.teacher = self.teachers[self.view.get_teacher()]