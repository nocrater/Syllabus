from dto.human_dto import HumanDTO
from repository.human_repository import HumanRepository
from service.service import CRUDService


class HumanService(CRUDService):
    def __init__(self):
        super().__init__(HumanDTO, HumanRepository())