from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pj_repository import PJRepository
from src.controllers.pj_withdraw_controller import PJWithdrawController
from src.views.pj_withdraw_view import PJWithdrawView


def pj_withdraw_composer():
    model = PJRepository(db_connection_handler)
    controller = PJWithdrawController(model)
    view = PJWithdrawView(controller)

    return view
