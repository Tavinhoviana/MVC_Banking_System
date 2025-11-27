from src.controllers.interfaces.pf_lister_controller import PFListerControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PFListerView(ViewInterface):
    def __init__(self, controller: PFListerControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()

        return HttpResponse(status_code=200, body=body_response)
