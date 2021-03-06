from dto.human_dto import HumanDTO


class StudentDTO(HumanDTO):
    def __init__(self, first_name=None, second_name=None, patronymic=None, date=None, klas=None, id=None):
        super().__init__(first_name, second_name, patronymic, date, id)

    def __str__(self):
        return f'Фамилия: {self.first_name} Имя: {self.second_name} Отчество: {self.patronymic} ' \
               f'Дата рождения: {self.date}'
