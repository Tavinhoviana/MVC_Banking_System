from typing import List
from src.models.sqlite.entities.pf import PFTable
from .pf_lister_controller import PFListerController

class MockPFRepository:
    def list_pf(self):
        return [
            PFTable(nome_completo="Guinga", categoria="platinum", id=4),
            PFTable(nome_completo="Djalma", categoria="ferro", id=7)
        ]

def test_list_pf():
    controller = PFListerController(MockPFRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "PF",
            "count": 2,
            "attributes": [
                { "nome": "Guinga", "id": 4 },
                { "nome": "Djalma", "id": 7 }
            ]
        }
    }
    
    assert response == expected_response
