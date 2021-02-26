from PyQt5.QtWidgets import QWidget

from registry.registry import Registry


class Presenter:
    def __init__(self, view: QWidget) -> None:
        self.view = view

    def remove_widget(self) -> None:
        Registry.get_instance().get_main_presenter().remove_widget(self.view)
