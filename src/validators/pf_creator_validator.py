from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def pf_creator_validator(http_request: HttpRequest) -> None:
    
    class BodyData(BaseModel):
        renda_mensal: int
        idade: int
        nome_completo: constr(min_length=1) #type: ignore
        celular: int
        email: constr(min_length=1) #type: ignore
        categoria: constr(min_length=1) #type: ignore
        saldo: int

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
