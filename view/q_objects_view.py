from abc import abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QPushButton, QHBoxLayout, QHeaderView

from presenters.contracts import IObjectsPresenter
from view.contracts import IObjectsView


class QObjectsView(QWidget):
    __meta_class__ = IObjectsView

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.add_button = QPushButton("Новая запись", self)
        self.add_button.clicked.connect(self.add)
        self.edit_button = QPushButton('Редактировать', self)
        self.edit_button.clicked.connect(self.edit)
        self.del_button = QPushButton('Удалить', self)
        self.del_button.clicked.connect(self.delete)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_button)
        btn_layout.addWidget(self.edit_button)
        btn_layout.addWidget(self.del_button)

        self.table = QTableWidget(self)
        self.init_table()
        self.table.doubleClicked.connect(self.edit)

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.presenter = None

    def set_presenter(self, presenter: IObjectsPresenter):
        self.presenter = presenter

    def get_presenter(self):
        return self.presenter

    @abstractmethod
    def init_table(self):
        pass

    def add(self):
        self.presenter.add()

    def delete(self):
        self.presenter.delete()

    def edit(self):
        self.presenter.edit()

    def set_table_row(self, row):
        self.table.setRowCount(row)

    def set_item(self, row, col, value):
        item = QTableWidgetItem(value)
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.table.setItem(row, col, item)

    def get_selected_row_index(self):
        lst = self.table.selectedIndexes()
        if not lst:
            return None
        return lst[0].row()

    def remove_row(self, index):
        self.table.removeRow(index)

    def add_row(self):
        self.table.setRowCount(self.table.rowCount() + 1)