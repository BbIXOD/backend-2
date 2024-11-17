from flask import Blueprint, request, jsonify, abort
from db.DataController import DataController
from db.entities import UserSchema

api = Blueprint("user", __name__)
db = DataController("db/users.csv", ["id", "name"])

@api.route("/user/<user_id>", methods=["GET", "DELETE"])
def user_action_id(user_id):
    user = db.find(user_id) if request.method == "GET" else db.remove(user_id)
    if not user: abort(404)
    return jsonify(user)

@api.route("/user", methods=["POST"])
def add_user():
    try:
        user_schema = UserSchema()
        params = user_schema.load(request.json)

        added = db.add(*params.values())
        if not added: abort(409)
        return jsonify(record_schema.dump(params)), 201
    except:
        return jsonify({"errors": err.messages}), 400


@api.route("/users")
def get_all_users():
    return jsonify(db.readAll())
