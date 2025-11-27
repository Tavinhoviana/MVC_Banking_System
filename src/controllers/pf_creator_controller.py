from typing import Dict
import re
from src.models.sqlite.interfaces.pf_repository_interfaces import PFRepositoryInteface
from .interfaces.pf_creator_controller import PFCreatorControllerInterface

class PFCreatorController(PFCreatorControllerInterface):
    def __init__(self, pf_repository: PFRepositoryInteface) -> None:
        self.__pf_repository = pf_repository

    def create(self, person_info: Dict) -> Dict:
        nome_completo = person_info["nome_completo"]
        renda_mensal = person_info["renda_mensal"]
        idade = person_info["idade"]
        celular = person_info["celular"]
        email = person_info["email"]
        categoria = person_info["categoria"]
        saldo = person_info["saldo"]

        self.__validate_nome_completo(nome_completo)
        self.__insert_person_in_db(nome_completo, renda_mensal, idade, celular, email, categoria, saldo)
        formated_response = self.__format_response(person_info)
        return formated_response

    def __validate_nome_completo(self: str, nome_completo: str) -> None:
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(nome_completo):
            raise Exception ("Invalid name")
    
    def __insert_person_in_db(self: str, nome_completo: str, renda_mensal: int, idade: int, celular: int, email: str, categoria: str, saldo: int) -> None:
        self.__pf_repository.create_pf(nome_completo, renda_mensal, idade, celular, email, categoria, saldo)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
