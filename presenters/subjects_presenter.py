from dto.subject_dto import SubjectDTO
from presenters.objects_presenter import ObjectsPresenter
from service.subject_service import SubjectService
from view.contracts import IObjectsView
from view.q_subject_view import QSubjectView


class SubjectsPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, SubjectService,  QSubjectView, SubjectDTO)

    def fill_row(self, row: int, obj: SubjectDTO) -> None:
        self.view.set_item(row, 0, obj.name)
        self.service.load_teacher(obj)
        self.view.set_item(row, 1, obj.teacher.full_name())
