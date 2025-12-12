from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.pf_creator_composer import pf_creator_composer
from src.main.composer.pf_withdraw_composer import pf_withdraw_composer

pf_route_bp = Blueprint("pf", __name__)

@pf_route_bp.route("/pf", methods=["GET"])
def list_pfs():
    return jsonify({"message": "Olá Terra"}), 200

@pf_route_bp.route("/pf", methods=["POST"])
def create_pfs():
    http_request = HttpRequest(body=request.json)
    view = pf_creator_composer()
    
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pf_route_bp.route("/pf/withdraw", methods=["POST"])
def pf_withdraw():
    http_request = HttpRequest(body=request.json)
    view = pf_withdraw_composer()
    
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

