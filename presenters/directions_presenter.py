from dto.direction_dto import DirectionDTO
from presenters.objects_presenter import ObjectsPresenter
from service.direction_service import DirectionService
from view.contracts import IObjectsView
from view.q_direction_view import QDirectionView


class DirectionsPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, DirectionService,  QDirectionView, DirectionDTO)

    def fill_row(self, row: int, obj: DirectionDTO) -> None:
        self.view.set_item(row, 0, obj.name)
