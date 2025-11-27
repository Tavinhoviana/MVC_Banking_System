from typing import List
from src.models.sqlite.entities.pj import PJTable
from .pj_lister_controller import PJListerController

class MockPJRepository:
    def list_pj(self):
        return [
            PJTable(nome_completo="Guinga", categoria="platinum", id=4),
            PJTable(nome_completo="Djalma", categoria="ferro", id=7)
        ]

def test_list_pj():
    controller = PJListerController(MockPJRepository())
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
