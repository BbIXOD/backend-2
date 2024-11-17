from flask import Blueprint, request, jsonify, abort
from data_utils.DataController import DataController
from datetime import datetime
from data_utils.entities import RecordSchema

api = Blueprint("record", __name__)
db = DataController("data_utils/records.csv", ["id", "user_id", "category_id", "timestamp", "spent"])

@api.route("/", methods=["GET", "POST"])
def record_action():
    if request.method == "GET":
        user_id = request.args.get("user_id")
        category_id = request.args.get("category_id")
        if not user_id and not category_id: abort(400)
        
        records, close = db.read()
        filtered = []
        for record in records:
            user_match = user_id and record["user_id"] == user_id
            category_match = category_id and record["category_id"]
            if user_match and category_match:
                filtered.append(record)
        return jsonify(filtered)


    try:
        record_schema = RecordSchema()
        params = record_schema.load(request.json)
        params["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        added = db.add(*params.values())
        if not added:
            abort(409)
        return jsonify(record_schema.dump(params)), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

@api.route("/<record_id>", methods=["GET", "DELETE"])
def record_id_action(record_id):
    record = db.find(record_id) if request.method == "GET" else db.remove(record_id)
    if not record: abort(404)
    return jsonify(record)

