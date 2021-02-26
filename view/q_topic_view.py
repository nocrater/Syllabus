from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QListWidget, QLineEdit, QSpinBox, QVBoxLayout, QListWidgetItem, \
    QPushButton, QHBoxLayout

from presenters.topic_presenter import TopicPresenter


class QTopicView(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        name_label = QLabel("Название", self)
        self.name_edit = QLineEdit(self)

        subjects_label = QLabel("Темы", self)
        self.subjects_list = QListWidget(self)

        layout = QVBoxLayout()       
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(subjects_label)
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

        self.presenter = TopicPresenter(self)

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

    def set_name(self, name):
        self.name_edit.setText(name)

    def get_name(self):
        return self.name_edit.text()
    
    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
