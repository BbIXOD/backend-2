from flask import Blueprint, request, jsonify, abort
from db.DataController import DataController

api = Blueprint("user", __name__)
db = DataController("db/users.csv", ["id", "name"])

@api.route("/user/<user_id>", methods=["GET", "DELETE"])
def user_action_id(user_id):
    user = db.find(user_id) if request.method == "GET" else db.remove(user_id)
    if not user: abort(404)
    return jsonify(user)

@api.route("/user", methods=["POST"])
def add_user():
    json = request.json
    id = json.get("id")
    name = json.get("name")

    added = db.add(id, name)
    if not added: abort(409)
    return {"id": id, "name": name}, 201

@api.route("/users")
def get_all_users():
    return jsonify(db.readAll())
