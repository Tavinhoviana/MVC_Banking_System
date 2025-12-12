from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pj_repository import PJRepository
from src.controllers.pj_finder_controller import PJFinderController
from src.views.pj_finder_view import PJFinderView

def pj_finder_composer():
    model = PJRepository(db_connection_handler)
    controller = PJFinderController(model)
    view = PJFinderView(controller)

    return view
