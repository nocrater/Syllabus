from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.results_presenter import ResultsPresenter
from view.q_objects_view import QObjectsView


class QResultsView (QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(ResultsPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Ученик', 'Предмет', 'Оценка', 'Число'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)