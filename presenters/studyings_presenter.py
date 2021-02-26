from dto.studying_dto import StudyingDTO
from presenters.objects_presenter import ObjectsPresenter
from service.studying_service import StudyingService
from view.contracts import IObjectsView
from view.q_studying_view import QStudyingView


class StudyingsPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, StudyingService,  QStudyingView, StudyingDTO)

    def fill_row(self, row: int, obj: StudyingDTO) -> None:
        self.service.load_subjects(obj)
        self.view.set_item(row, 0, str(obj.beginning_time))
        self.view.set_item(row, 1, str(obj.date))
        self.view.set_item(row, 2, ', '.join(map(lambda item: item.name, obj.subjects)))
        

