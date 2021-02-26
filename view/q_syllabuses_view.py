from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.syllabuses_presenter import SyllabusesPresenter
from view.q_objects_view import QObjectsView


class QSyllabusesView(QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(SyllabusesPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Начало', 'Конец', 'Расписание'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)