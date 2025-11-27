from typing import Dict, List
from src.models.sqlite.entities.pj import PJTable
from src.models.sqlite.interfaces.pj_repository_interfaces import PJRepositoryInterface
from .interfaces.pj_lister_controller import PJListerControllerInterface

class PJListerController(PJListerControllerInterface):
    def __init__(self, pj_repository: PJRepositoryInterface):
        self.__pj_repository = pj_repository

    def list(self) -> Dict:
        pj = self.__get_pf_in_db()
        response = self.__format_response(pj)
        return response

    def __get_pf_in_db(self) -> List[PJTable]:
        return self.__pj_repository.list_pj()
    
    def __format_response(self, pjs: List[PJTable]) -> Dict:
        formated_pj = []
        for pj in pjs:
            formated_pj.append({ "nome": pj.nome_completo, "id": pj.id })
        
        return {
            "data": {
                "type": "PF",
                "count": len(formated_pj),
                "attributes": formated_pj
            }
        }
