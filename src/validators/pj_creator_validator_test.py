from .pj_creator_validator import pj_creator_validator

class MockRequest:
    def __init__(self, body):
        self.body = body

def test_pf_creator_validator():
    request = MockRequest({
        "renda_mensal": 5500,
        "idade": 24,
        "nome_completo": "fulano de tal",
        "celular": 3538264445,
        "email": "fulanodetal@gmail.com",
        "categoria": "ouro",
        "saldo": 55000
    })

    pj_creator_validator(request)
