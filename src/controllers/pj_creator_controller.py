from typing import Dict
import re
from src.models.sqlite.interfaces.pj_repository_interfaces import PJRepositoryInterface
from .interfaces.pj_creator_controller import PJCreatorControllerInterface
from src.errors.error_types.http_bad_request import HttpBadRequestError

class PJCreatorController(PJCreatorControllerInterface):
    def __init__(self, pj_repository: PJRepositoryInterface) -> None:
        self.__pj_repository = pj_repository

    def create(self, person_info: Dict) -> Dict:
        nome_completo = person_info["nome_completo"]
        renda_mensal = person_info["renda_mensal"]
        idade = person_info["idade"]
        celular = person_info["celular"]
        email = person_info["email"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]

        self.__validate_nome_completo(nome_completo)
        self.__insert_person_in_db(
            nome_completo, renda_mensal, idade, celular, email, categoria, saldo
        )
        
        return self.__format_response(person_info)

    def __validate_nome_completo(self, nome_completo: str) -> None:
        pattern = re.compile(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$')
        if not pattern.match(nome_completo):
            raise HttpBadRequestError("Invalid name")

    def __insert_person_in_db(
        self,
        nome_completo: str,
        renda_mensal: int,
        idade: int,
        celular: str,
        email: str,
        categoria: str,
        saldo: int
    ) -> None:
        self.__pj_repository.create_pj(
            renda_mensal=renda_mensal,
            idade=idade,
            nome_completo=nome_completo,
            celular=celular,
            email=email,
            categoria=categoria,
            saldo=saldo
        )

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
