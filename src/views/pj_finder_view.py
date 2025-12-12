from src.controllers.interfaces.pj_finder_controller import PJFinderControllerInterface
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PJFinderView(ViewInterface):
    def __init__(self, controller: PJFinderControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pj_id = http_request.param["pj_id"]
        body_response = self.__controller.find(pj_id)

        return HttpResponse(status_code=200, body=body_response)
