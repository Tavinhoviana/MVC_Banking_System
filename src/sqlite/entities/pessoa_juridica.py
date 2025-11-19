from sqlalchemy import Column, String, BIGINT, REAL
from src.sqlite.settings.base import Base

class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL, nullable=False)
    idade = Column(BIGINT, nullable=False)
    nome_completo = Column(String, nullable=True)
    celular = Column(String, nullable=False)
    email = Column(String, nullable=True)
    categoria = Column(String, nullable=True)
    saldo = Column(REAL, nullable=False)

    def __repr__(self):
        return (
        f"Pessoa juridica [\n"
        f"  nome_completo={self.nome_completo},\n"
        f"  idade={self.idade},\n"
        f"  celular={self.celular},\n"
        f"  email={self.email},\n"
        f"  categoria={self.categoria}\n"
        f"]"
    )
