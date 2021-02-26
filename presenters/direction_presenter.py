from presenters.object_presenter import ObjectPresenter
from service.direction_service import DirectionService
from view.contracts import IDirectionView


class DirectionPresenter(ObjectPresenter):
    def __init__(self, view: IDirectionView) -> None:
        ObjectPresenter.__init__(self, view, DirectionService)

    def to_view(self):
        self.view.set_name(self.object.name)

    def from_view(self):
        self.object.name = self.view.get_name()