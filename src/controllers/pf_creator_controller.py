from src.models.sqlite.interfaces.pf_repository_interfaces import PFRepositoryInteface

class PFCreatorController:
    def __init__(self, pf_repository: PFRepositoryInteface) -> None:
        self.__pf_repository = pf_repository
