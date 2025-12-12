from typing import Dict
from src.models.sqlite.interfaces.pj_repository_interfaces import PJRepositoryInterface
from src.models.sqlite.entities.pj import PJTable
from .interfaces.pj_finder_controller import PJFinderControllerInterface
from src.errors.error_types.http_not_found import HttpNotFoundError


class PJFinderController(PJFinderControllerInterface):
    def __init__(self, pj_repository: PJRepositoryInterface) -> None:
        self.__pj_repository = pj_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PJTable:
        person = self.__pj_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("People not found")

        return person

    def __format_response(self, person: PJTable) -> Dict:
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
