from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pf import PFTable
from src.models.sqlite.interfaces.pf_repository_interfaces import PFRepositoryInteface

class PFRepository(PFRepositoryInteface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def list_pf(self) -> List[PFTable]:
        with self.__db_connection as database:
            try:
                pf = database.session.query(PFTable).all()
                return pf
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
            
    def get_person(self, person_id: int) -> PFTable:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(PFTable)
                    .filter(PFTable.id == person_id)
                    .one()
                )
                return person
            except NoResultFound:
                return None