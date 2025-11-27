from typing import Dict
from src.models.sqlite.interfaces.pf_repository_interfaces import PFRepositoryInteface
from src.models.sqlite.entities.pf import PFTable
from .interfaces.pf_finder_controller import PFFinderControllerInterface

class PFFinderController(PFFinderControllerInterface):
    def __init__(self, pf_repository: PFRepositoryInteface) -> None:
        self.__pf_repository = pf_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PFTable:
        person = self.__pf_repository.get_person(person_id)
        if not person:
            raise Exception("People not found")

        return person

    def __format_response(self, person: PFTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "nome_completo": person.nome_completo,
                    "renda_mensal": person.renda_mensal,
                    "idade": person.idade,
                    "celular": person.celular,
                    "email": person.email,
                    "categoria": person.categoria,
                    "saldo": person.saldo
                }
            }
        }
