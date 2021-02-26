from abc import ABC, abstractmethod

from dto.dto import DTO


class IMainPresenter(ABC):
    @abstractmethod
    def show_directions(self) -> None:
        pass

    @abstractmethod
    def add_widget(self, widget) -> None:
        pass

    @abstractmethod
    def remove_widget(self, widget) -> None:
        pass


class ICallBack(ABC):
    @abstractmethod
    def call(self) -> None:
        pass


class IObjectsPresenter(ABC):
    @abstractmethod
    def add(self) -> None:
        pass

    @abstractmethod
    def edit(self) -> None:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass


class IObjectPresenter(ABC):
    @abstractmethod
    def set_object(self, obj: DTO) -> None:
        pass

    @abstractmethod
    def set_callback(self, callback: ICallBack) -> None:
        pass

    @abstractmethod
    def ok(self) -> None:
        pass

    @abstractmethod
    def cancel(self) -> None:
        pass

    @abstractmethod
    def is_ok(self) -> bool:
        pass
