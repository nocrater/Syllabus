from PyQt5.QtWidgets import QHeaderView, QWidget

from presenters.klases_presenter import KlassesPresenter
from view.q_objects_view import QObjectsView


class QKlasesView(QObjectsView):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        QObjectsView.__init__(self, parent)
        self.set_presenter(KlassesPresenter(view=self))

    def init_table(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Дата создания', 'Класс', 'Направление', 'Учебный план', 'Ученики'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)