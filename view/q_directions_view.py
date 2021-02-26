from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.directions_presenter import DirectionsPresenter
from view.q_objects_view import QObjectsView


class QDirectionsView (QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(DirectionsPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Название'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)