from dto.topic_dto import TopicDTO
from presenters.objects_presenter import ObjectsPresenter
from service.topic_service import TopicService
from view.contracts import IObjectsView
from view.q_topic_view import QTopicView


class TopicsPresenter(ObjectsPresenter):
    def __init__(self, view: IObjectsView) -> None:
        ObjectsPresenter.__init__(self, view, TopicService,  QTopicView, TopicDTO)

    def fill_row(self, row: int, obj: TopicDTO) -> None:
        self.service.load_subjects(obj)
        self.view.set_item(row, 0, obj.name)
        self.view.set_item(row, 1, ', '.join(map(lambda item: item.name, obj.subjects)))
        

