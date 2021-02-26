from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit

from presenters.result_presenter import ResultPresenter
from view.contracts import IResultView


class QResultView(QWidget):

    __meta_class__ = IResultView

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        self.student_label = QLabel("Ученик", parent=self)
        self.student_cmb = QComboBox(parent=self)

        self.topic_label = QLabel("Предмет", parent=self)
        self.topic_cmb = QComboBox(parent=self)
        
        self.label = QLabel('Оценка', parent=self)
        self.mark = QLineEdit(parent=self)

        self.date_label = QLabel("Дата", parent=self)
        self.date_edit = QDateEdit(calendarPopup=True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.student_label)
        layout.addWidget(self.student_cmb)
        layout.addWidget(self.topic_label)
        layout.addWidget(self.topic_cmb)
        layout.addWidget(self.label)
        layout.addWidget(self.mark)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_edit)

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

        self.presenter = ResultPresenter(view=self)

    def set_student_items(self, items: str):
        self.student_cmb.addItems(items)

    def set_student(self, name):
        self.student_cmb.setCurrentText(name)

    def get_student(self):
        return self.student_cmb.currentText()

    def set_topic_items(self, items: str):
        self.topic_cmb.addItems(items)

    def set_topic(self, name):
        self.topic_cmb.setCurrentText(name)

    def get_topic(self):
        return self.topic_cmb.currentText()

    def get_mark(self):
        return self.mark.text()

    def set_mark(self, value):
        if value is not None:
            self.mark.setText(str(value))

    def get_date(self):
        return self.date_edit.date().toPyDate()

    def set_date(self, value):
        if value is not None:
            self.date_edit.setDate(value)

    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
