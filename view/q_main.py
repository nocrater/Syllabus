from PyQt5.QtWidgets import QMainWindow, qApp, QAction, QStackedWidget, QWidget

from presenters.contracts import IMainPresenter
from presenters.main_presenter import MainPresenter
from view.contracts import IMainView


class QMain(QMainWindow):

    __meta_class__ = IMainView

    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.stacked_widget = None
        self.menu = None
        self.entities = None
        self.set_ui()
        self.presenter = MainPresenter(self)

    def set_ui(self) -> None:
        self.create_menu()
        self.setWindowTitle("Управление")
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.8)
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

    def create_menu(self) -> None:
        self.menu = self.menuBar()
        self.entities = self.menu.addMenu("Сущности")

        direction_action = QAction('Направления', self)
        self.entities.addAction(direction_action)
        direction_action.triggered.connect(self.show_directions)

        student_action = QAction('Ученики', self)
        self.entities.addAction(student_action)
        student_action.triggered.connect(self.show_students)

        teacher_action = QAction('Учителя', self)
        self.entities.addAction(teacher_action)
        teacher_action.triggered.connect(self.show_teachers)

        subject_action = QAction('Темы', self)
        self.entities.addAction(subject_action)
        subject_action.triggered.connect(self.show_subjects)

        topic_action = QAction('Предметы', self)
        self.entities.addAction(topic_action)
        topic_action.triggered.connect(self.show_topics)

        result_action = QAction('Результаты', self)
        self.entities.addAction(result_action)
        result_action.triggered.connect(self.show_results)

        studying_action = QAction('Уроки на день', self)
        self.entities.addAction(studying_action)
        studying_action.triggered.connect(self.show_studyings)

        syllabus_action = QAction('Учебный план', self)
        self.entities.addAction(syllabus_action)
        syllabus_action.triggered.connect(self.show_syllabuses)

        klass_action = QAction('Классы', self)
        self.entities.addAction(klass_action)
        klass_action.triggered.connect(self.show_klases)

    def add_central_widget(self, widget: QWidget) -> None:
        self.stacked_widget.addWidget(widget)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.count() - 1)

    def remove_central_widget(self, widget: QWidget) -> None:
        self.stacked_widget.removeWidget(widget)

    def show_directions(self) -> None:
        self.presenter.show_directions()

    def show_students(self) -> None:
        self.presenter.show_students()

    def show_teachers(self) -> None:
        self.presenter.show_teachers()

    def show_subjects(self) -> None:
        self.presenter.show_subjects()

    def show_topics(self) -> None:
        self.presenter.show_topics()

    def show_results(self) -> None:
        self.presenter.show_results()

    def show_studyings(self) -> None:
        self.presenter.show_studyings()

    def show_syllabuses(self) -> None:
        self.presenter.show_syllabuses()

    def show_klases(self) -> None:
        self.presenter.show_klases()

    def get_presenter(self) -> IMainPresenter:
        return self.presenter

