from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pj_repository import PJRepository
from src.controllers.pj_creator_controller import PJCreatorController
from src.views.pj_creator_view import PJCreatorView


def pj_creator_composer():
    model = PJRepository(db_connection_handler)
    controller = PJCreatorController(model)
    view = PJCreatorView(controller)

    return view
