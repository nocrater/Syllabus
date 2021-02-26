from abc import abstractmethod

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QDateEdit

from view.contracts import IHumanView


class QHumanView(QWidget):
    __meta_class__ = IHumanView

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.first_name_label = QLabel('Имя', parent=self)
        self.first_name_edit = QLineEdit(parent=self)

        self.second_name_label = QLabel("Фамилия", parent=self)
        self.second_name_edit = QLineEdit(parent=self)

        self.patronymic_label = QLabel("Отчество", parent=self)
        self.patronymic_edit = QLineEdit(parent=self)

        self.date_label = QLabel("Дата рождения", parent=self)
        self.date_edit = QDateEdit(calendarPopup=True)

        layout = QVBoxLayout()
        layout.addWidget(self.second_name_label)
        layout.addWidget(self.second_name_edit)
        layout.addWidget(self.first_name_label)
        layout.addWidget(self.first_name_edit)
        layout.addWidget(self.patronymic_label)
        layout.addWidget(self.patronymic_edit)
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

    def get_first_name(self):
        return self.first_name_edit.text()

    def set_first_name(self, value):
        self.first_name_edit.setText(value)

    def get_second_name(self):
        return self.second_name_edit.text()

    def set_second_name(self, value):
        self.second_name_edit.setText(value)

    def get_patronymic(self):
        return self.patronymic_edit.text()

    def set_patronymic(self, value):
        self.patronymic_edit.setText(value)

    def get_date(self):
        return self.date_edit.date().toPyDate()

    def set_date(self, value):
        if value is not None:
            self.date_edit.setDate(value)

    @abstractmethod
    def ok(self):
        pass

    @abstractmethod
    def cancel(self):
        pass
