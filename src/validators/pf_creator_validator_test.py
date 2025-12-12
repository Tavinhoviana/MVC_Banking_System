from .pf_creator_validator import pf_creator_validator

class MockRequest:
    def __init__(self, body):
        self.body = body

def test_pf_creator_validator():
    request = MockRequest({
        "renda_mensal": 1200,
        "idade": 24,
        "nome_completo": "fulano de tal",
        "celular": 3538264445,
        "email": "fulanodetal@gmail.com",
        "categoria": "bronze",
        "saldo": 2400
    })

    pf_creator_validator(request)
