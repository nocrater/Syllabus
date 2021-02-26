from presenters.object_presenter import ObjectPresenter
from view.contracts import IHumanView


class HumanPresenter(ObjectPresenter):
    def __init__(self, view: IHumanView, service_class) -> None:
        ObjectPresenter.__init__(self, view, service_class)

    def to_view(self):
        self.view.set_first_name(self.object.first_name)
        self.view.set_second_name(self.object.second_name)
        self.view.set_patronymic(self.object.patronymic)
        self.view.set_date(self.object.date)

    def from_view(self):
        self.object.first_name = self.view.get_first_name()
        self.object.second_name = self.view.get_second_name()
        self.object.patronymic = self.view.get_patronymic()
        self.object.date = self.view.get_date()
