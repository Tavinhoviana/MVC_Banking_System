from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pf import PFTable

class PFRepositoryInterface(ABC):

    @abstractmethod
    def list_pf(self) -> List[PFTable]:
        pass

    @abstractmethod
    def create_pf(
        self,
        renda_mensal: int,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: int
    ) -> None:
        pass
