from abc import ABC, abstractmethod

class ClienteInterface(ABC):

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

    @abstractmethod
    def extrato(self) -> dict:
        pass
