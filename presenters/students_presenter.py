from dto.student_dto import StudentDTO
from presenters.objects_presenter import ObjectsPresenter
from service.student_service import StudentService
from view.contracts import IObjectsView
from view.q_student_view import QStudentView


class StudentsPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, StudentService,  QStudentView, StudentDTO)

    def fill_row(self, row: int, obj: StudentDTO) -> None:
        self.view.set_item(row, 0, obj.full_name())
        self.view.set_item(row, 1, str(obj.date))

