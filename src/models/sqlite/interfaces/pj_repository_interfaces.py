from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pj import PJTable

class PJRepositoryInterface(ABC):

    @abstractmethod
    def list_pj(self) -> List[PJTable]:
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