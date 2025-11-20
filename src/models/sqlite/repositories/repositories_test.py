import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pj_repository import PJRepository
from .pf_repository import PFRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interaction with DB")
def test_list_pj():
    repo = PJRepository(db_connection_handler)
    response = repo.list_pj()
    print(response)

@pytest.mark.skip(reason="Interaction with DB")
def test_list_pf():
    repo = PFRepository(db_connection_handler)
    response = repo.list_pf()
    print(response)

@pytest.mark.skip(reason="Interaction with DB")
def test_create_pf():
    renda_mensal = 1200
    idade = 28
    nome_completo = "Otavio Viana"
    celular = "+49 176 20008117"
    email = "otavio_viana@hotmail.com"
    categoria = "bronze"
    saldo = 10000

    repo = PFRepository(db_connection_handler)
    repo.create_pf(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

@pytest.mark.skip(reason="Interaction with DB")
def test_create_pj():
    renda_mensal = 5000
    idade = 33
    nome_completo = "Guinga Cancun"
    celular = "+55 11 96368-3670"
    email = "guinga_cancun69@hotmail.com"
    categoria = "platinum"
    saldo = 10000

    repo = PJRepository(db_connection_handler)
    repo.create_pj(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
