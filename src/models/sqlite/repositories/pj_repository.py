from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pj import PJTable
from src.models.sqlite.interfaces.pj_repository_interfaces import PJRepositoryInterface

class PJRepository(PJRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def list_pj(self) -> List[PJTable]:
        with self.__db_connection as database:
            try:
                pj = database.session.query(PJTable).all()
                return pj
            except NoResultFound:
                return []
            
    def create_pj(
        self,
        renda_mensal: int,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: int
    ) -> None:
        with self.__db_connection as database:
            try:
                person_data = PJTable(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_person(self, person_id: int) -> PJTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(PJTable)
                    .filter(PJTable.id == person_id)
                    .one()
                )
                return person
            except NoResultFound:
                return None