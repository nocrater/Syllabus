from dto.result_dto import ResultDTO
from presenters.objects_presenter import ObjectsPresenter
from service.result_service import ResultService
from view.contracts import IObjectsView
from view.q_result_view import QResultView


class ResultsPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, ResultService,  QResultView, ResultDTO)

    def fill_row(self, row: int, obj: ResultDTO) -> None:
        self.service.load_student(obj)
        self.view.set_item(row, 0, obj.student.full_name())
        self.view.set_item(row, 1, obj.topic.name)
        self.view.set_item(row, 2, str(obj.mark))
        self.view.set_item(row, 3, str(obj.date))
