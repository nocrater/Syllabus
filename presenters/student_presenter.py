from presenters.object_presenter import ObjectPresenter
from presenters.human_presenter import HumanPresenter
from service.student_service import StudentService
from view.contracts import IStudentView


class StudentPresenter(HumanPresenter):
    def __init__(self, view: IStudentView) -> None:
        ObjectPresenter.__init__(self, view, StudentService)
