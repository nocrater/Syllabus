from dto.klas_dto import KlasDTO
from presenters.objects_presenter import ObjectsPresenter
from service.klas_service import KlasService
from view.contracts import IObjectsView
from view.q_klas_view import QKlasView


class KlassesPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, KlasService,  QKlasView, KlasDTO)

    def fill_row(self, row: int, obj: KlasDTO) -> None:
        self.service.load_direction(obj)
        self.service.load_syllabus(obj)
        self.service.load_students(obj)
        self.view.set_item(row, 0, str(obj.date))
        self.view.set_item(row, 1, obj.number + ' ' + obj.letter)
        self.view.set_item(row, 2, obj.direction.name)
        self.view.set_item(row, 3, str(obj.syllabus))
        self.view.set_item(row, 4, ', '.join(map(lambda item: item.full_name(), obj.students)))
        

