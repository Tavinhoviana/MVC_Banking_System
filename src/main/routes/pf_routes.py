from flask import Blueprint, jsonify

pf_route_bp = Blueprint("pf", __name__)

@pf_route_bp.route("/pf", methods=["GET"])
def list_pjs():
    return jsonify({"message": "Olá Terra"}), 200

