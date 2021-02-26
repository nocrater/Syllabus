from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, \
    QPushButton, QHBoxLayout, QDateEdit

from presenters.syllabus_presenter import SyllabusPresenter


class QSyllabusView(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        start_label = QLabel("Начало", self)
        self.start_edit = QDateEdit(calendarPopup=True)

        finish_label = QLabel("Конец", self)
        self.finish_edit = QDateEdit(calendarPopup=True)

        studyings_label = QLabel("Расписание", self)
        self.studyings_list = QListWidget(self)

        layout = QVBoxLayout()       
        layout.addWidget(start_label)
        layout.addWidget(self.start_edit)
        layout.addWidget(finish_label)
        layout.addWidget(self.finish_edit)
        layout.addWidget(studyings_label)
        layout.addWidget(self.studyings_list)

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

        self.presenter = SyllabusPresenter(self)

    def set_studying_items(self, items: str):
        for i in items:
            item = QListWidgetItem(i)
            item.setCheckState(Qt.Unchecked)
            self.studyings_list.addItem(item) 

    def set_studyings(self, studyings):
        if not studyings:
            return
        for i in studyings:
            self.studyings_list.findItems(i, Qt.MatchFixedString)[0].setData(Qt.CheckStateRole, Qt.Checked)

    def get_studyings(self):
        return [self.studyings_list.item(i).text() for i in range(self.studyings_list.count())
                if self.studyings_list.item(i).checkState() == Qt.Checked]

    def get_start(self):
        return self.start_edit.date().toPyDate()

    def set_start(self, value):
        if value is not None:
            self.start_edit.setDate(value)

    def get_finish(self):
        return self.finish_edit.date().toPyDate()

    def set_finish(self, value):
        if value is not None:
            self.finish_edit.setDate(value)
    
    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
