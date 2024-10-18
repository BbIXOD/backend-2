from flask import Flask, jsonify
#from routes import api

app = Flask(__name__)


#app.register_blueprint(api, url_prefix='/api')

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Working"})

if __name__ == '__main__':
    app.run(debug=True)
