from service.service import CRUDService
from dto.direction_dto import DirectionDTO
from repository.direction_repository import DirectionRepository

class DirectionService(CRUDService):
    def __init__(self):
        super().__init__(DirectionDTO, DirectionRepository())