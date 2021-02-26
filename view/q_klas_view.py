from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, \
    QPushButton, QHBoxLayout, QDateEdit, QLineEdit, QComboBox

from presenters.klas_presenter import KlasPresenter


class QKlasView(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.date_label = QLabel("Дата создания", self)
        self.date_edit = QDateEdit(calendarPopup=True)

        self.letter_label = QLabel("Буква", self)
        self.letter_edit = QLineEdit(self)

        self.direction_label = QLabel("Направление", parent=self)
        self.direction_cmb = QComboBox(parent=self)

        self.syllabus_label = QLabel("Учебный план", parent=self)
        self.syllabus_cmb = QComboBox(parent=self)

        self.students_label = QLabel("Ученики", self)
        self.students_list = QListWidget(self)

        layout = QVBoxLayout()       
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_edit)
        layout.addWidget(self.letter_label)
        layout.addWidget(self.letter_edit)
        layout.addWidget(self.direction_label)
        layout.addWidget(self.direction_cmb)
        layout.addWidget(self.syllabus_label)
        layout.addWidget(self.syllabus_cmb)
        layout.addWidget(self.students_label)
        layout.addWidget(self.students_list)

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

        self.presenter = KlasPresenter(self)

    def set_direction_items(self, items: str):
        self.direction_cmb.addItems(items)

    def set_direction(self, name):
        self.direction_cmb.setCurrentText(name)

    def get_direction(self):
        return self.direction_cmb.currentText()

    def set_syllabus_items(self, items: str):
        self.syllabus_cmb.addItems(items)

    def set_syllabus(self, name):
        self.syllabus_cmb.setCurrentText(name)

    def get_syllabus(self):
        return self.syllabus_cmb.currentText()
    
    def set_student_items(self, items: str):
        for i in items:
            item = QListWidgetItem(i)
            item.setCheckState(Qt.Unchecked)
            self.students_list.addItem(item)

    def set_students(self, students):
        if not students:
            return
        for i in students:
            self.students_list.findItems(i, Qt.MatchFixedString)[0].setData(Qt.CheckStateRole, Qt.Checked)

    def get_students(self):
        return [self.students_list.item(i).text() for i in range(self.students_list.count())
                if self.students_list.item(i).checkState() == Qt.Checked]

    def get_date(self):
        return self.date_edit.date().toPyDate()

    def set_date(self, value):
        if value is not None:
            self.date_edit.setDate(value)

    def get_letter(self):
        return self.letter_edit.text()

    def set_letter(self, value):
        self.letter_edit.setText(value)
    
    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
