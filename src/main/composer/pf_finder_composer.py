from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pf_repository import PFRepository
from src.controllers.pf_finder_controller import PFFinderController
from src.views.pf_finder_view import PFFinderView

def pf_finder_composer():
    model = PFRepository(db_connection_handler)
    controller = PFFinderController(model)
    view = PFFinderView(controller)

    return view
