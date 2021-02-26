from presenters.object_presenter import ObjectPresenter
from service.subject_service import SubjectService
from service.studying_service import StudyingService
from view.contracts import IStudyingView


class StudyingPresenter(ObjectPresenter):
    def __init__(self, view: IStudyingView) -> None:
        ObjectPresenter.__init__(self, view, StudyingService)
        self.subjects = {i.name: i for i in SubjectService().get_all()}
        self.view.set_subject_items(self.subjects.keys())

    def to_view(self):
        self.view.set_time(self.object.beginning_time)
        self.view.set_date(self.object.date)
        if self.object.subjects:
            self.view.set_subjects([i.name for i in self.object.subjects])

    def from_view(self):
        self.object.beginning_time = self.view.get_time()
        self.object.date = self.view.get_date()
        self.object.subjects = [self.subjects[i] for i in self.view.get_subjects()]

