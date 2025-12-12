from typing import Dict
from src.models.sqlite.interfaces.pf_repository_interfaces import PFRepositoryInterface

class PFWithdrawController:
    def __init__(self, pf_repository: PFRepositoryInterface) -> None:
        self.__pf_repository = pf_repository

    def withdraw(self, data: Dict) -> Dict:
        person_id = data["id"]
        amount = data["valor"]

        person = self.__pf_repository.get_person(person_id)
        if not person:
            raise Exception("Pessoa física não encontrada")

        if not person.sacar(amount):
            raise Exception("Saque não permitido")

        self.__pf_repository.update_pf(person)

        return {
            "message": "Saque realizado com sucesso",
            "saldo_atual": person.saldo
        }
