from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_route():
    return jsonify("Hello World! Welcome to my Flask Application.")


@app.route("/greet/<name>", methods=["GET"])
def greet_route(name):
    return jsonify(f"Hello, {name}!")


@app.route("/farewell/<name>", methods=["GET"])
def farewell_route(name):
    return jsonify(f"Goodbye, {name}!")


if __name__ == "__main__":
    app.run()
