import pytest
from .pj_creator_controller import PJCreatorController

class MockPJRepository:
    def create_pj(self: str, nome_completo: str, renda_mensal: int, idade: int, celular: int, email: str, categoria: str, saldo: int):
        pass

def test_create():
    person_infos = {
        "nome_completo": "GuingaMilionario",
        "renda_mensal": 5000,
        "idade": 20,
        "celular": 11969699696,
        "email": "guinga_rico@gmail.com",
        "categoria": "platinum",
        "saldo": 15000
    }

    controller = PJCreatorController(MockPJRepository())
    response = controller.create(person_infos)

    assert response["data"] ["type"] == "Person"
    assert response["data"] ["count"] == 1
    assert response["data"] ["attributes"] == person_infos

def test_create_error():
    person_infos = {
        "nome_completo": "Guinga Milionario",
        "renda_mensal": 5000,
        "idade": 20,
        "celular": 11969699696,
        "email": "guinga_rico@gmail.com",
        "categoria": "platinum",
        "saldo": 15000
    }

    controller = PJCreatorController(MockPJRepository())
    with pytest.raises(Exception):
        controller.create(person_infos)
