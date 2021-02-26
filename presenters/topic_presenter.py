from presenters.object_presenter import ObjectPresenter
from service.subject_service import SubjectService
from service.topic_service import TopicService
from view.contracts import ITopicView


class TopicPresenter(ObjectPresenter):
    def __init__(self, view: ITopicView) -> None:
        ObjectPresenter.__init__(self, view, TopicService)
        self.subjects = {i.name: i for i in SubjectService().get_all()}
        self.view.set_subject_items(self.subjects.keys())

    def to_view(self):
        self.view.set_name(self.object.name)
        if self.object.subjects:
            self.view.set_subjects([i.name for i in self.object.subjects])

    def from_view(self):
        self.object.name = self.view.get_name()
        self.object.subjects = [self.subjects[i] for i in self.view.get_subjects()]

