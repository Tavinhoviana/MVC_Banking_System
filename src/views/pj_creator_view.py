from src.controllers.interfaces.pj_creator_controller import PJCreatorControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.validators.pj_creator_validator import pj_creator_validator


class PJCreatorView(ViewInterface):
    def __init__(self, controller: PJCreatorControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pj_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
