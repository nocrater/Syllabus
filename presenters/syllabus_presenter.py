from presenters.object_presenter import ObjectPresenter
from service.studying_service import StudyingService
from service.syllabus_service import SyllabusService
from view.contracts import ISyllabusView


class SyllabusPresenter(ObjectPresenter):
    def __init__(self, view: ISyllabusView) -> None:
        ObjectPresenter.__init__(self, view, SyllabusService)
        self.studyings = {i.title(): i for i in StudyingService().get_all()}
        self.view.set_studying_items(self.studyings.keys())

    def to_view(self):
        if self.object.studyings:
            self.view.set_studyings([i.title() for i in self.object.studyings])
        self.view.set_start(self.object.start)
        self.view.set_finish(self.object.finish)

    def from_view(self):
        self.object.studyings = [self.studyings[i] for i in self.view.get_studyings()]
        self.object.start = self.view.get_start()
        self.object.finish = self.view.get_finish()

