from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.topics_presenter import TopicsPresenter
from view.q_objects_view import QObjectsView


class QTopicsView(QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(TopicsPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Название', 'Темы'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)