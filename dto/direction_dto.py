from dto.dto import DTO

class DirectionDTO(DTO):
    classes = {'klas': 'KlasDTO'}

    def __init__(self, name=None, id=None):
        self.id = id
        self.name = name

    @staticmethod
    def class_by_name(name):
        return DirectionDTO.classes[name]

    def __str__(self):
        return f'direction: {self.name}'