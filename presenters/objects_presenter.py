from abc import abstractmethod

from dto.dto import DTO
from presenters.contracts import IObjectsPresenter, ICallBack
from presenters.presenter import Presenter
from registry.registry import Registry
from view.contracts import IObjectsView


class ObjectsPresenter(Presenter, IObjectsPresenter, ICallBack):
    def __init__(self, view: IObjectsView, service_class, edit_view_class, dto_class):
        Presenter.__init__(self, view)
        self.service = service_class()
        self.edit_view_class = edit_view_class
        self.dto_class = dto_class
        self.objects = self.service.get_all()
        self.fill_table()

        self.edit_view = self.edit_view_class(self.view)
        self.edit_presenter = self.edit_view.get_presenter()
        self.edit_presenter.set_callback(self)

        self.current_object = None

    def fill_table(self) -> None:
        self.view.set_table_row(len(self.objects))
        for r, p in enumerate(self.objects):
            self.fill_row(r, p)

    @abstractmethod
    def fill_row(self, row: int, obj: DTO) -> None:
        pass

    def add(self) -> None:
        self.current_object = self.dto_class()
        self.edit_presenter.set_object(self.current_object)
        Registry.get_instance().get_main_presenter().add_widget(self.edit_view)

    def edit(self) -> None:
        index = self.view.get_selected_row_index()
        if index is not None:
            self.current_object = self.objects[index]
            self.edit_presenter.set_object(self.current_object)
            Registry.get_instance().get_main_presenter().add_widget(self.edit_view)

    def delete(self) -> None:
        index = self.view.get_selected_row_index()
        if index is not None:
            self.service.delete(self.objects[index])
            self.view.remove_row(index)
            del self.objects[index]

    def call(self) -> None:
        edit_presenter = self.edit_view.get_presenter()
        if edit_presenter.is_ok():
            if self.current_object in self.objects:
                self.fill_row(self.objects.index(self.current_object), self.current_object)
            else:
                self.objects.append(self.current_object)
                self.view.add_row()
                self.fill_row(len(self.objects) - 1, self.current_object)
            self.current_object = None
