import pytest
from unittest import mock
from src.models.sqlite.entities.pj import PJTable
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .pj_repository import PJRepository

class MockConnection:
    def __init__(self) -> None:
        self.session= UnifiedAlchemyMagicMock(
            data= [
                (
                    [mock.call.query(PJTable)], # query
                    [PJTable(nome_completo="nome_completo", celular="celular")] # result
                )
            ]
        )
    
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session= UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")
    
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

@pytest.mark.skip(reason="Interaction with DB")
def test_list_pj():
    mock_connection = MockConnection()
    repo = PJRepository(mock_connection)
    response = repo.list_pj()

    mock_connection.session.query.assert_called_once_with(PJTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()
    
    assert response[0].nome_completo == "nome_completo"

@pytest.mark.skip(reason="Interaction with DB")
def test_list_pj_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PJRepository(mock_connection)
    response = repo.list_pj()

    mock_connection.session.query.assert_called_once_with(PJTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()
    
    assert response == []

def update_pj(self, person):
    self.person = person