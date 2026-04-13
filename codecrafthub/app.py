from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
# This enables CORS for all routes and all origins by default
CORS(app) 

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "courses.json")
ALLOWED_STATUSES = {"Not Started", "In Progress", "Completed"}

# Ensure data directory and file exist
os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f, indent=2)

def load_data():
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def find_course(course_id, data):
    for c in data:
        if c.get("id") == course_id:
            return c
    return None

def validate_date(date_str):
    try:
        datetime.fromisoformat(date_str)
        # Basic format check: YYYY-MM-DD
        # fromisoformat accepts more than this, but we rely on user providing YYYY-MM-DD
        return True
    except ValueError:
        return False


# Get next available ID
def get_next_id(data):
    if not data:
        return 1
    return max(int(course['id']) for course in data) + 1

@app.route("/api/courses", methods=["GET"])
def get_courses():
    data = load_data()
    return jsonify(data), 200

@app.route("/api/courses/<course_id>", methods=["GET"])
def get_course(course_id):
    data = load_data()
    course = find_course(course_id, data)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify(course), 200

@app.route("/api/courses", methods=["POST"])
def create_course():
    data = load_data()
    payload = request.get_json(silent=True)

    if not payload:
        return jsonify({"error": "Request must be JSON"}), 400

    id = str(get_next_id(data))
    name = payload.get("name")
    description = payload.get("description")
    target_date = payload.get("target_date")
    status = payload.get("status", "Not Started")

    if not id:
        id = "1"

    if not name or not description or not target_date:
        return jsonify({"error": "Missing required fields: name, description, target_date"}), 400

    if not validate_date(target_date):
        return jsonify({"error": "target_date must be a valid date in YYYY-MM-DD format"}), 400

    if status not in ALLOWED_STATUSES:
        return jsonify({"error": f"status must be one of {sorted(ALLOWED_STATUSES)}"}), 400

    new_course = {
        "id": id,
        "name": name,
        "description": description,
        "target_date": target_date,
        "status": status
    }

    data.append(new_course)
    save_data(data)
    return jsonify(new_course), 201

@app.route("/api/courses/<course_id>", methods=["PUT"])
def update_course(course_id):
    data = load_data()
    course = find_course(course_id, data)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({"error": "Request must be JSON"}), 400

    name = payload.get("name")
    description = payload.get("description")
    target_date = payload.get("target_date")
    status = payload.get("status")

    if name is not None:
        course["name"] = name
    if description is not None:
        course["description"] = description
    if target_date is not None:
        if not validate_date(target_date):
            return jsonify({"error": "target_date must be a valid date in YYYY-MM-DD format"}), 400
        course["target_date"] = target_date
    if status is not None:
        if status not in ALLOWED_STATUSES:
            return jsonify({"error": f"status must be one of {sorted(ALLOWED_STATUSES)}"}), 400
        course["status"] = status

    save_data(data)
    return jsonify(course), 200

@app.route("/api/courses/<course_id>", methods=["DELETE"])
def delete_course(course_id):
    data = load_data()
    course = find_course(course_id, data)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    data = [c for c in data if c.get("id") != course_id]
    save_data(data)
    return "", 204

if __name__ == '__main__':
    print("CodeCraftHub API is starting...")
    print(f"Data will be stored in: {os.path.abspath(DATA_FILE)}")
    print("API will be available at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

