from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface

class PFWithdrawView(ViewInterface):
    def __init__(self, controller):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            print("Body recebido no saque:", body)
            result = self.__controller.withdraw(body)
            return HttpResponse(status_code=200, body=result)

        except Exception as e:
            print("Erro no saque:", e)
            return HttpResponse(status_code=400, body={"error": str(e)})
