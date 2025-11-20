from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pj import PJTable
from src.models.sqlite.entities.pf import PFTable

class PFRepository:
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def list_pj(self) -> List[PJTable]:
        with self.__db_connection as database:
            try:
                pj = database.session.query(PJTable).all()
                return pj
            except NoResultFound:
                return []

    def create_pf(
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
                person_data = PFTable(
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
