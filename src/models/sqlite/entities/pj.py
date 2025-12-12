from sqlalchemy import Column, String, BIGINT, REAL
from src.models.sqlite.settings.base import Base
from src.models.sqlite.interfaces.clientes_interface import ClienteInterface

class PJTable(Base):
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

    LIMITE_SAQUE = 1500

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        if valor > self.LIMITE_SAQUE:
            return False
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def extrato(self) -> dict:
        
        return {
            "id": self.id,
            "nome_completo": self.nome_completo,
            "saldo_atual": self.saldo,
        }

    def __repr__(self):
        return (
            f"Pessoa física [\n"
            f"  nome_completo={self.nome_completo},\n"
            f"  idade={self.idade},\n"
            f"  celular={self.celular},\n"
            f"  email={self.email},\n"
            f"  categoria={self.categoria},\n"
            f"  saldo={self.saldo}\n"
            f"]"
        )
    
def processar_saque(cliente: ClienteInterface, valor: float):
    if cliente.sacar(valor):
        print("Saque efetuado.")
    else:
        print("Erro no saque.")