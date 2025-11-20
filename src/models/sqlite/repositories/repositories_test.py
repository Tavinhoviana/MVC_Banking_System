import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pj_repository import PJRepository

# db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interaction with DB")
def test_list_pj():
    repo = PJRepository(db_connection_handler)
    response = repo.list_pj()
    print(response)
