import pytest
from .pf_creator_controller import PFCreatorController

class MockPFRepository:
    def create_pf(self: str, nome_completo: str, renda_mensal: int, idade: int, celular: int, email: str, categoria: str, saldo: int):
        pass

def test_create():
    person_infos = {
        "nome_completo": "Djalma Da Malasia",
        "renda_mensal": 1000,
        "idade": 18,
        "celular": 11963683670,
        "email": "djalma_malasiano@gmail.com",
        "categoria": "ferro",
        "saldo": 5000
    }

    controller = PFCreatorController(MockPFRepository())
    response = controller.create(person_infos)

    assert response["data"] ["type"] == "Person"
    assert response["data"] ["count"] == 1
    assert response["data"] ["attributes"] == person_infos

def test_create_error():
    person_infos = {
        "nome_completo": "Djalma123",
        "renda_mensal": 1000,
        "idade": 18,
        "celular": 11963683670,
        "email": "djalma_malasiano@gmail.com",
        "categoria": "ferro",
        "saldo": 5000
    }

    controller = PFCreatorController(MockPFRepository())
    with pytest.raises(Exception):
        controller.create(person_infos)
