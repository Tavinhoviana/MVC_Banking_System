from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pj_creator_composer import pj_creator_composer
from src.main.composer.pj_withdraw_composer import pj_withdraw_composer
from src.main.composer.pj_finder_composer import pj_finder_composer

from src.errors.error_handler import handle_errors

pj_route_bp = Blueprint("pj", __name__)

@pj_route_bp.route("/pj", methods=["GET"])
def list_pjs():
    return jsonify({"message": "Olá Terra"}), 200

@pj_route_bp.route("/pj", methods=["POST"])
def create_pjs():
    try:
        http_request = HttpRequest(body=request.json)
        view = pj_creator_composer()
        
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pj_route_bp.route("/pj/withdraw", methods=["POST"])
def pj_withdraw():
    try:
        http_request = HttpRequest(body=request.json)
        view = pj_withdraw_composer()
        
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pj_route_bp.route("/pj/<pj_id>", methods=["GET"])
def find_pj(pj_id):
    try:
        http_request = HttpRequest(param={"pj_id": pj_id})
        view = pj_finder_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
