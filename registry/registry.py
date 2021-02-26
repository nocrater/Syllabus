from presenters.contracts import IMainPresenter


class Registry:
    _instance = None

    def __init__(self) -> None:
        self.main_presenter = None

    @staticmethod
    def get_instance():
        if not Registry._instance:
            Registry._instance = Registry()
        return Registry._instance

    def set_main_presenter(self, presenter: IMainPresenter) -> None:
        self.main_presenter = presenter

    def get_main_presenter(self) -> None:
        return self.main_presenter
