from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pj import PJTable

class PJRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    
    def list_pj(self) -> List[PJTable]:
        with self.__db_connection as database:
            try:
                pj = database.session.query(PJTable).all()
                return pj
            except NoResultFound:
                return []

    # def create_pj(self) -> None:
    #     with self.__db_connection as database:
    #         try: 
                