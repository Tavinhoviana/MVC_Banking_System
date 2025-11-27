from .pf_finder_controller import PFFinderController

class MockPerson():
    def __init__(self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo) -> None:
        self.renda_mensal = renda_mensal
        self.nome_completo = nome_completo
        self.idade = idade
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo

class MockPFRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            renda_mensal= 1000,
            idade= 20,
            nome_completo= "Guinga Rico",
            celular= 1196969699696,
            email= "guinga_rico@gmail.com",
            categoria= "platinum",
            saldo= 5000
        )
        
def test_find():
    controller = PFFinderController(MockPFRepository())
    response = controller.find(123)

    excepted_response = {
        "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "renda_mensal": 1000,
                    "idade": 20,
                    "nome_completo": "Guinga Rico",
                    "celular": 1196969699696,
                    "email": "guinga_rico@gmail.com",
                    "categoria": "platinum",
                    "saldo": 5000
                }
            }
    }

    assert response == excepted_response
