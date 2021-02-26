from abc import ABC, abstractmethod

from PyQt5.QtWidgets import QWidget, QMessageBox

from dto.dto import DTO
from presenters.contracts import ICallBack, IObjectPresenter
from presenters.presenter import Presenter


class ObjectPresenter(Presenter, IObjectPresenter):
    def __init__(self, view: QWidget, service_class) -> None:
        Presenter.__init__(self, view=view)
        self.object = None
        self.ok_flag = False
        self.callback = None
        self.service = service_class()

    def set_object(self, obj: DTO) -> None:
        self.object = obj
        self.to_view()

    def set_callback(self, callback: ICallBack) -> None:
        self.callback = callback

    def ok(self) -> None:
        self.from_view()
        self.ok_flag = True
        try:
            if self.object.id:
                self.service.update(self.object)
            else:
                self.service.create(self.object)
            self.remove_widget()
            self.callback.call()
        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Поля записи некорректны")
            msg.setWindowTitle("Error")
            msg.exec_()


    def cancel(self) -> None:
        self.ok_flag = False
        self.remove_widget()
        self.callback.call()

    def is_ok(self) -> bool:
        return self.ok_flag

    @abstractmethod
    def to_view(self) -> None:
        pass

    @abstractmethod
    def from_view(self) -> None:
        pass