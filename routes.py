from flask import Blueprint, request, jsonify, abort

api = Blueprint("routes", __name__)

@api.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    file = open("db/users.csv", "r")
    lines = file.readlines()

    for line in lines:
        [ id, name ] = line.split(",")
        if id != user_id: continue

        return jsonify({"id": id, "name": name.rstrip()})
    
    abort(404)

