from dto.dto import DTO


class HumanDTO(DTO):
    def __init__(self, first_name=None, second_name=None, patronymic=None, date=None, id=None):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.patronymic = patronymic
        self.date = date

    def full_name(self):
        return f'{self.second_name} {self.first_name} {self.patronymic}'
