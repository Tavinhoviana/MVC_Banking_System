from flask import Blueprint, jsonify

pj_route_bp = Blueprint("pj", __name__)

@pj_route_bp.route("/pj", methods=["GET"])
def list_pjs():
    return jsonify({"message": "Olá Mundo"}), 200
