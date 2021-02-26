from dto.syllabus_dto import SyllabusDTO
from presenters.objects_presenter import ObjectsPresenter
from service.syllabus_service import SyllabusService
from view.contracts import IObjectsView
from view.q_syllabus_view import QSyllabusView


class SyllabusesPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, SyllabusService,  QSyllabusView, SyllabusDTO)

    def fill_row(self, row: int, obj: SyllabusDTO) -> None:
        self.service.load_studyings(obj)
        self.view.set_item(row, 0, str(obj.start))
        self.view.set_item(row, 1, str(obj.finish))
        self.view.set_item(row, 2, ', '.join(map(lambda item: item.title(), obj.studyings)))
        

