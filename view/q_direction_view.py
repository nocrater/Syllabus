from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

from presenters.direction_presenter import DirectionPresenter
from view.contracts import IDirectionView


class QDirectionView(QWidget):

    __meta_class__ = IDirectionView

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.label = QLabel('Название', parent=self)
        self.name = QLineEdit(parent=self)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.name)

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

        self.presenter = DirectionPresenter(view=self)

    def get_name(self):
        return self.name.text()

    def set_name(self, value):
        self.name.setText(value)

    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
