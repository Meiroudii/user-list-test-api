from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

# @app.route is a decorator
@app.route("/")
def home():
    if request.method == "POST":
        return "Go back kid"
    return "home"

# Path parameter is user-id
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
            "user_id": user_id,
            "name": "John Doe",
            "email": "john.doe@example.com"
            }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    # Check if what method is use
    data = request.get_json()

    # TODO: ADD into database
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
    # serve(app)
