from presenters.object_presenter import ObjectPresenter
from service.result_service import ResultService
from service.student_service import StudentService
from service.topic_service import TopicService
from view.contracts import IResultView


class ResultPresenter(ObjectPresenter):
    def __init__(self, view: IResultView) -> None:
        ObjectPresenter.__init__(self, view, ResultService)
        self.students = {i.full_name(): i for i in StudentService().get_all()}
        self.view.set_student_items(self.students.keys())

        self.topics = {i.name: i for i in TopicService().get_all()}
        self.view.set_topic_items(self.topics.keys())

    def to_view(self):
        if self.object.student:
            self.view.set_student(self.object.student.full_name())
        if self.object.topic:
            self.view.set_topic(self.object.topic.name)
        self.view.set_mark(self.object.mark)
        self.view.set_date(self.object.date)

    def from_view(self):
        self.object.student = self.students[self.view.get_student()]
        self.object.topic = self.topics[self.view.get_topic()]
        self.object.mark = self.view.get_mark()
        self.object.date = self.view.get_date()