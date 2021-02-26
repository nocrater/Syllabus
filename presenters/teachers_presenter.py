from dto.teacher_dto import TeacherDTO
from presenters.objects_presenter import ObjectsPresenter
from service.teacher_service import TeacherService
from view.contracts import IObjectsView
from view.q_teacher_view import QTeacherView


class TeachersPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, TeacherService,  QTeacherView, TeacherDTO)

    def fill_row(self, row: int, obj: TeacherDTO) -> None:
        self.view.set_item(row, 0, obj.full_name())
        self.view.set_item(row, 1, str(obj.date))

