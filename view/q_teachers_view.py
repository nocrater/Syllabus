from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.teachers_presenter import TeachersPresenter
from view.q_objects_view import QObjectsView


class QTeachersView(QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(TeachersPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ФИО', 'Дата рождения'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
