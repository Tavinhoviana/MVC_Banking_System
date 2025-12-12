from src.controllers.interfaces.pf_finder_controller import PFFinderControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PFFinderView(ViewInterface):
    def __init__(self, controller: PFFinderControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pf_id = http_request.param["pf_id"]
        body_response = self.__controller.find(pf_id)

        return HttpResponse(status_code=200, body=body_response)
