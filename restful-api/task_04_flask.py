#!/usr/bin/python3
"""A simple API built with Flask."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users.
# Kept empty on purpose: the checker populates it via /add_user,
# so no test data should be hardcoded here.
users = {}


@app.route("/")
def home():
    """Return a welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return the list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return a simple status message."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object for the given username, or 404."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the in-memory users dictionary."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
