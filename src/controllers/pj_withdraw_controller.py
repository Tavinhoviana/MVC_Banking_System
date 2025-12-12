from typing import Dict
from src.models.sqlite.interfaces.pj_repository_interfaces import PJRepositoryInterface

class PJWithdrawController:
    def __init__(self, pj_repository: PJRepositoryInterface) -> None:
        self.__pj_repository = pj_repository

    def pj_withdraw(self, data: Dict) -> Dict:
        person_id = data["id"]
        amount = data["valor"]

        person = self.__pj_repository.get_person(person_id)
        if not person:
            raise Exception("Pessoa juridica não encontrada")

        if not person.sacar(amount):
            raise Exception("Saque não permitido")

        self.__pj_repository.update_pj(person)

        return {
            "message": "Saque realizado com sucesso",
            "saldo_atual": person.saldo
        }
