from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox

from presenters.subject_presenter import SubjectPresenter
from view.contracts import ISubjectView


class QSubjectView(QWidget):

    __meta_class__ = ISubjectView

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.label = QLabel('Название', parent=self)
        self.name = QLineEdit(parent=self)

        self.teacher_label = QLabel("Учитель", parent=self)
        self.teacher_cmb = QComboBox(parent=self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name)
        layout.addWidget(self.teacher_label)
        layout.addWidget(self.teacher_cmb)

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

        self.presenter = SubjectPresenter(view=self)

    def get_name(self):
        return self.name.text()

    def set_name(self, value):
        self.name.setText(value)

    def set_teacher_items(self, items: str):
        self.teacher_cmb.addItems(items)

    def set_teacher(self, name):
        self.teacher_cmb.setCurrentText(name)

    def get_teacher(self):
        return self.teacher_cmb.currentText()

    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
