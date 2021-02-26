from datetime import time

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QListWidget, QLineEdit, QSpinBox, QVBoxLayout, QListWidgetItem, \
    QPushButton, QHBoxLayout, QTimeEdit, QDateEdit

from presenters.studying_presenter import StudyingPresenter


class QStudyingView(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.time_label = QLabel("Время начала", self)
        self.time_edit = QTimeEdit()

        self.date_label = QLabel("Дата", parent=self)
        self.date_edit = QDateEdit(calendarPopup=True)

        self.subjects_label = QLabel("Темы", self)
        self.subjects_list = QListWidget(self)

        layout = QVBoxLayout()       
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_edit)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_edit)
        layout.addWidget(self.subjects_label)
        layout.addWidget(self.subjects_list)

        self.ok_btn = QPushButton('OK', parent=self)
        self.ok_btn.clicked.connect(self.ok)
        self.ok_cancel = QPushButton('Cancel', parent=self)
        self.ok_cancel.clicked.connect(self.cancel)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.ok_btn)
        btn_layout.addWidget(self.ok_cancel)

        layout.addLayout(btn_layout)
        layout.addStretch(0)

        self.setLayout(layout)

        self.presenter = StudyingPresenter(self)

    def set_subject_items(self, items: str):
        for i in items:
            item = QListWidgetItem(i)
            item.setCheckState(Qt.Unchecked)
            self.subjects_list.addItem(item)

    def set_subjects(self, subjects):
        if not subjects:
            return
        for i in subjects:
            self.subjects_list.findItems(i, Qt.MatchFixedString)[0].setData(Qt.CheckStateRole, Qt.Checked)

    def get_subjects(self):
        return [self.subjects_list.item(i).text() for i in range(self.subjects_list.count())
                if self.subjects_list.item(i).checkState() == Qt.Checked]

    def get_time(self):
        return self.time_edit.time().toPyTime()

    def set_time(self, value):
        if value is not None:
            self.time_edit.setTime(value)

    def get_date(self):
        return self.date_edit.date().toPyDate()

    def set_date(self, value):
        if value is not None:
            self.date_edit.setTime(value)
    
    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
