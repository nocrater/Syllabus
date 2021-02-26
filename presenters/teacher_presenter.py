from presenters.object_presenter import ObjectPresenter
from presenters.human_presenter import HumanPresenter
from service.teacher_service import TeacherService
from view.contracts import ITeacherView


class TeacherPresenter(HumanPresenter):
    def __init__(self, view: ITeacherView) -> None:
        ObjectPresenter.__init__(self, view, TeacherService)
