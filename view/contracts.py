from abc import ABC, abstractmethod
from datetime import date

from PyQt5.QtWidgets import QWidget

from presenters.contracts import IObjectPresenter, IObjectsPresenter


class IMainView(ABC):
    @abstractmethod
    def add_central_widget(self, widget: QWidget) -> None:
        pass

    @abstractmethod
    def remove_central_widget(self, widget: QWidget) -> None:
        pass


class IObjectsView(ABC):
    @abstractmethod
    def set_table_row(self, row: int) -> None:
        pass

    @abstractmethod
    def set_item(self, row: int, col: int, value: str) -> None:
        pass

    @abstractmethod
    def get_selected_row_index(self) -> int:
        pass

    @abstractmethod
    def remove_row(self, index: int) -> None:
        pass

    @abstractmethod
    def add_row(self) -> None:
        pass

    @abstractmethod
    def get_presenter(self) -> IObjectsPresenter:
        pass


class IDirectionView(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, value: str) -> None:
        pass

    @abstractmethod
    def get_presenter(self) -> IObjectPresenter:
        pass


class IHumanView(ABC):
    @abstractmethod
    def get_first_name(self) -> str:
        pass

    @abstractmethod
    def set_first_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_second_name(self) -> str:
        pass

    @abstractmethod
    def set_second_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_patronymic(self) -> str:
        pass

    @abstractmethod
    def set_patronymic(self, name: str) -> None:
        pass

    @abstractmethod
    def get_presenter(self) -> IObjectPresenter:
        pass

    @abstractmethod
    def get_date(self) -> date:
        pass

    @abstractmethod
    def set_date(self, value: date) -> None:
        pass


class IStudentView(IHumanView, ABC):
    pass


class ITeacherView(IHumanView, ABC):
    pass


class ISubjectView(IHumanView, ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_teacher(self) -> str:
        pass

    @abstractmethod
    def set_teacher(self, index: str) -> None:
        pass


class ITopicView(ABC):
    @abstractmethod
    def set_subject_items(self, items: str):
        pass

    @abstractmethod
    def set_subjects(self, authors):
        pass

    @abstractmethod
    def get_subjects(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_name(self):
        pass


class IResultView(ABC):
    @abstractmethod
    def set_student_items(self, items: str):
        pass

    @abstractmethod
    def get_student(self) -> str:
        pass

    @abstractmethod
    def set_student(self, index: str) -> None:
        pass

    @abstractmethod
    def set_topic_items(self, items: str):
        pass

    @abstractmethod
    def get_topic(self) -> str:
        pass

    @abstractmethod
    def set_topic(self, index: str) -> None:
        pass

    @abstractmethod
    def get_mark(self) -> str:
        pass

    @abstractmethod
    def set_mark(self, mark: str) -> None:
        pass

    @abstractmethod
    def get_date(self) -> date:
        pass

    @abstractmethod
    def set_date(self, value: date) -> None:
        pass


class IStudyingView(ABC):
    @abstractmethod
    def set_subject_items(self, items: str):
        pass

    @abstractmethod
    def set_subjects(self, authors):
        pass

    @abstractmethod
    def get_subjects(self):
        pass

    @abstractmethod
    def set_time(self, time):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def get_date(self) -> date:
        pass

    @abstractmethod
    def set_date(self, value: date) -> None:
        pass

class ISyllabusView(ABC):
    @abstractmethod
    def set_studying_items(self, items: str):
        pass

    @abstractmethod
    def set_studyings(self, authors):
        pass

    @abstractmethod
    def get_studyings(self):
        pass

    @abstractmethod
    def set_start(self, start):
        pass

    @abstractmethod
    def get_start(self):
        pass

    @abstractmethod
    def set_finish(self, finish):
        pass

    @abstractmethod
    def get_finish(self):
        pass


class IKlasView(ABC):
    @abstractmethod
    def set_direction_items(self, items: str):
        pass

    @abstractmethod
    def set_directions(self, authors):
        pass

    @abstractmethod
    def get_directions(self):
        pass

    @abstractmethod
    def set_syllabus_items(self, items: str):
        pass

    @abstractmethod
    def set_syllabuses(self, authors):
        pass

    @abstractmethod
    def get_syllabuses(self):
        pass

    @abstractmethod
    def set_student_items(self, items: str):
        pass

    @abstractmethod
    def set_students(self, authors):
        pass

    @abstractmethod
    def get_students(self):
        pass

    @abstractmethod
    def get_date(self) -> date:
        pass

    @abstractmethod
    def set_date(self, value: date) -> None:
        pass

    @abstractmethod
    def set_letter(self, letter):
        pass

    @abstractmethod
    def get_letter(self):
        pass