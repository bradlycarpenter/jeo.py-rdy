from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/", methods=['GET'])
def hello_world():
    return "Yo mams gay"

if __name__ == "__main__":
    app.run(debug=True)
