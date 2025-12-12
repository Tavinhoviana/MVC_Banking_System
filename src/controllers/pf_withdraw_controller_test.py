import pytest
from .pf_withdraw_controller import PFWithdrawController

class MockPFRepository:
    def __init__(self):
        self.person = type("Person", (), {"saldo": 5000, "sacar": lambda self, amount: amount <= self.saldo})()
    
    def get_person(self, person_id):
        if person_id == 1:
            return self.person
        return None

    def update_pf(self, person):
        self.person = person

def test_withdraw_success():
    controller = PFWithdrawController(MockPFRepository())
    
    data = {"id": 1, "valor": 500}
    response = controller.withdraw(data)
    
    assert response["message"] == "Saque realizado com sucesso"
    assert response["saldo_atual"] == 5000

def test_withdraw_person_not_found():
    controller = PFWithdrawController(MockPFRepository())
    
    data = {"id": 999, "valor": 1000}
    with pytest.raises(Exception, match="Pessoa física não encontrada"):
        controller.withdraw(data)

def test_withdraw_not_allowed():
    class MockRepo:
        def __init__(self):
            self.person = type("Person", (), {"saldo": 500, "sacar": lambda self, amount: False})()
        def get_person(self, person_id):
            return self.person
        def update_pf(self, person):
            pass
    
    controller = PFWithdrawController(MockRepo())
    data = {"id": 1, "valor": 501}
    
    with pytest.raises(Exception, match="Saque não permitido"):
        controller.withdraw(data)
