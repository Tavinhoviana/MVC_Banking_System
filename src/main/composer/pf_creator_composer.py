from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pf_repository import PFRepository
from src.controllers.pf_creator_controller import PFCreatorController
from src.views.pf_creator_view import PFCreatorView

def pf_creator_composer():
    model = PFRepository(db_connection_handler)
    controller = PFCreatorController(model)
    view = PFCreatorView(controller)

    return view
