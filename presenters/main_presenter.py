from PyQt5.QtWidgets import QWidget

from presenters.contracts import IMainPresenter
from view.contracts import IMainView
from view.q_directions_view import QDirectionsView
from view.q_klases_view import QKlasesView
from view.q_students_view import QStudentsView
from view.q_teachers_view import QTeachersView
from view.q_subjects_view import QSubjectsView
from view.q_topics_view import QTopicsView
from view.q_results_view import QResultsView
from view.q_studyings_view import QStudyingsView
from view.q_syllabuses_view import QSyllabusesView


class MainPresenter(IMainPresenter):
    def __init__(self, view: IMainView) -> None:
        self.view = view

    def show_directions(self) -> None:
        self.view.add_central_widget(QDirectionsView(self.view))

    def show_students(self) -> None:
        self.view.add_central_widget(QStudentsView(self.view))

    def show_teachers(self) -> None:
        self.view.add_central_widget(QTeachersView(self.view))

    def show_subjects(self) -> None:
        self.view.add_central_widget(QSubjectsView(self.view))

    def show_topics(self) -> None:
        self.view.add_central_widget(QTopicsView(self.view))

    def show_results(self) -> None:
        self.view.add_central_widget(QResultsView(self.view))

    def show_studyings(self) -> None:
        self.view.add_central_widget(QStudyingsView(self.view))

    def show_syllabuses(self) -> None:
        self.view.add_central_widget(QSyllabusesView(self.view))

    def show_klases(self) -> None:
        self.view.add_central_widget(QKlasesView(self.view))

    def add_widget(self, widget: QWidget) -> None:
        self.view.add_central_widget(widget)

    def remove_widget(self, widget: QWidget) -> None:
        self.view.remove_central_widget(widget)

