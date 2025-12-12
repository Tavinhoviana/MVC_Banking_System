from src.controllers.interfaces.pf_creator_controller import PFCreatorControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.validators.pf_creator_validator import pf_creator_validator

class PFCreatorView(ViewInterface):
    def __init__(self, controller: PFCreatorControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pf_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
