from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PJWithdrawView(ViewInterface):
    def __init__(self, controller):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            result = self.__controller.pj_withdraw(body)
            return HttpResponse(status_code=200, body=result)
        except Exception as e:
            return HttpResponse(status_code=400, body={"error": str(e)})
