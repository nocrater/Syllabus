from PyQt5.QtWidgets import QLabel, QComboBox

from presenters.student_presenter import StudentPresenter
from view.q_human_view import QHumanView


class QStudentView(QHumanView):

    def __init__(self, parent=None):
        QHumanView.__init__(self, parent)

        self.presenter = StudentPresenter(self)

    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
