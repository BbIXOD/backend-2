from flask import Blueprint, request, jsonify, abort

api = Blueprint("routes", __name__)

@api.route("/user/<user_id>", methods=["GET", "DELETE"])
def get_user(user_id):
    if request.method == "DELETE":
        found = None
        file = []
        with open("db/users.csv", "r") as f: file = f.readlines()
        with open("db/users.csv", "w") as f:
            for line in file:
                [ id, name ] = line.split(",")
                if id != user_id: f.write(line)
                else: found = {"id": id, "name": name.rstrip()}
        
        if found == None: abort(404)
        return jsonify(found)


    with open("db/users.csv", "r") as file:
        for line in file:
            [ id, name ] = line.split(",")
            if id != user_id: continue
            return jsonify({"id": id, "name": name.rstrip()})

    abort(404)

@api.route("/user", methods=["POST"])
def add_user():
    json = request.json
    id = json.get("id")
    name = json.get("name")

    with open("db/users.csv", "r") as file:
        for line in file:
            if line.split(",")[0] == id:
                abort(409)

    with open("db/users.csv", "a") as file:
        file.write(f"{id},{name}\n")

    return {"id": id, "name": name}, 201

@api.route("/users")
def get_all_users():
    userlist = []
    with open("db/users.csv", "r") as file:
        for line in file:
            [ id, name ] = line.split(",")
            userlist.append({"id": id, "name": name.rstrip()})
    
    return jsonify(userlist)
