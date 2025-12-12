from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pf_repository import PFRepository
from src.controllers.pf_withdraw_controller import PFWithdrawController
from src.views.pf_withdraw_view import PFWithdrawView

def pf_withdraw_composer():
    model = PFRepository(db_connection_handler)
    controller = PFWithdrawController(model)
    view = PFWithdrawView(controller)

    return view
