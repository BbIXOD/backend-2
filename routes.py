from flask import Blueprint, request, jsonify

api = Blueprint("routes", __name__)

@api.route("/test", methods=["GET"])
def get_items():
    return jsonify([{"status": "working"}])