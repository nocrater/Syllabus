from PyQt5.QtWidgets import QLabel, QComboBox

from presenters.teacher_presenter import TeacherPresenter
from view.q_human_view import QHumanView


class QTeacherView(QHumanView):

    def __init__(self, parent=None):
        QHumanView.__init__(self, parent)

        self.presenter = TeacherPresenter(self)

    def ok(self):
        self.presenter.ok()

    def cancel(self):
        self.presenter.cancel()

    def get_presenter(self):
        return self.presenter
