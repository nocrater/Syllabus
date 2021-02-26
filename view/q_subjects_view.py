from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.subjects_presenter import SubjectsPresenter
from view.q_objects_view import QObjectsView


class QSubjectsView (QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(SubjectsPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Название', 'Учитель'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)