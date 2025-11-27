from typing import Dict, List
from src.models.sqlite.entities.pf import PFTable
from src.models.sqlite.interfaces.pf_repository_interfaces import PFRepositoryInteface
from .interfaces.pf_lister_controller import PFListerControllerInterface

class PFListerController(PFListerControllerInterface):
    def __init__(self, pf_repository: PFRepositoryInteface):
        self.__pf_repository = pf_repository

    def list(self) -> Dict:
        pf = self.__get_pf_in_db()
        response = self.__format_response(pf)
        return response

    def __get_pf_in_db(self) -> List[PFTable]:
        return self.__pf_repository.list_pf()
    
    def __format_response(self, pfs: List[PFTable]) -> Dict:
        formated_pf = []
        for pf in pfs:
            formated_pf.append({ "nome": pf.nome_completo, "id": pf.id })
        
        return {
            "data": {
                "type": "PF",
                "count": len(formated_pf),
                "attributes": formated_pf
            }
        }
