from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.studyings_presenter import StudyingsPresenter
from view.q_objects_view import QObjectsView


class QStudyingsView(QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(StudyingsPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Время начала', 'Число', 'Темы'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)