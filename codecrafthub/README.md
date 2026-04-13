This project was generated with AI
The front end was created with Bolt 
The back end was created with chatGTP-5 Nano
To run the back end do
pip3 install -r requirements.txt
python3 app.py


CodeCraftHub — A beginner-friendly REST API with Flask and a JSON data store



CodeCraftHub is a tiny, no-database learning project. It exposes a simple REST API built with Flask to manage a list of courses you want to learn. All data is stored in a JSON text file (data/courses.json). No authentication, no user management—just straightforward API basics to learn REST concepts.
1) Project overview

    Build a minimal learning platform to track courses
    Tech stack: Python + Flask
    Data storage: JSON file (no database)
    Endpoints cover the full CRUD workflow (Create, Read, Update, Delete)
    Validation for dates and statuses
    Suitable for beginners to practice REST API concepts

2) Features

    List all courses (GET /courses)
    Retrieve a single course (GET /courses/{id})
    Create a new course (POST /courses)
    Update an existing course (PUT /courses/{id})
    Delete a course (DELETE /courses/{id})
    Simple data validation:
        target_completion_date must be in YYYY-MM-DD
        status must be one of: Not Started, In Progress, Completed
    Data stored in data/courses.json (no database required)

Data model for a course:

    id: string (UUID)
    name: string
    description: string
    target_completion_date: string (YYYY-MM-DD)
    status: string (Not Started, In Progress, Completed)

3) Prerequisites

    Python 3.8+ (recommended)
    Basic knowledge of using the command line/terminal
    Optional: jq (for parsing JSON in shell)

4) Installation (step-by-step)

    Create the project folder (optional)

    mkdir CodeCraftHub
    cd CodeCraftHub

    Create a virtual environment (recommended)

    macOS/Linux:
        python3 -m venv venv
        source venv/bin/activate
    Windows:
        python -m venv venv
        .\venv\Scripts\activate

    Install dependencies

    pip3 install -r requirements.txt

    Ensure the data directory exists (the app creates it automatically if not)

    Start the application

    Python run (recommended for this project):
        python app.py
    Or using Flask CLI (if you prefer):
        export FLASK_APP=app.py
        export FLASK_ENV=development
        flask run
        Note: If you use the Flask CLI, you’ll access the API at http://127.0.0.1:5000 as well.

What you should see after starting:

    A Flask development server listening on http://127.0.0.1:5000

5) API endpoints documentation

Base URL: http://localhost:5000

    GET /courses
        Description: List all courses
        Response: 200 OK
        Example response: [ { "id": "2f6c8e4a-1234-5678-9abc-def012345678", "name": "Intro to Python", "description": "Learn Python basics", "target_completion_date": "2026-12-31", "status": "Not Started" } ]

    GET /courses/{id}
        Description: Retrieve a single course by its id
        Response: 200 OK (course), or 404 if not found
        Example response: { "id": "2f6c8e4a-1234-5678-9abc-def012345678", "name": "Intro to Python", "description": "Learn Python basics", "target_completion_date": "2026-12-31", "status": "Not Started" }

    POST /courses
        Description: Create a new course
        Request body (JSON): { "name": "Intro to Python", "description": "Learn Python basics", "target_completion_date": "2026-12-31", "status": "Not Started" // Optional; if omitted, defaults to "Not Started" }
        Required fields: name, description, target_completion_date
        Validates: date format, status value
        Response: 201 Created with the new course object
        Example response: { "id": "8a1f2c4e-9b0d-4a3f-9e8b-9f9f7d1a2b3c", "name": "Intro to Python", "description": "Learn Python basics", "target_completion_date": "2026-12-31", "status": "Not Started" }

    PUT /courses/{id}
        Description: Update fields of an existing course
        Request body (JSON): any subset of the fields { "name": "Intro to Python (Updated)", "description": "Updated description", "target_completion_date": "2027-01-15", "status": "In Progress" }
        Validation: date format if provided, status value if provided
        Response: 200 OK with the updated course object, or 404 if not found

    DELETE /courses/{id}
        Description: Delete a course
        Response: 204 No Content on success; 404 if not found
        Response body: empty

6) Testing instructions

Quick, copy-paste friendly tests using curl.

Base URL: http://localhost:5000

    Reset data to an empty list (start clean)

    Mac/Linux: echo [] > data/courses.json
    Windows (PowerShell): Set-Content -Path data/courses.json -Value '[]'

    List courses on an empty dataset

    curl -s -X GET http://localhost:5000/api/courses
    Expected: 200 and body: []

    Create a valid course (POST)

    curl -s -X POST -H "Content-Type: application/json"
    -d '{"name":"Intro to Python","description":"Learn Python basics","target_completion_date":"2026-12-31","status":"Not Started"}'
    http://localhost:5000/api/courses
    Expected: 201 and a JSON object with an id

    Retrieve the created course (GET)

    Replace <id> with the id from step 3
    curl -s -X GET http://localhost:5000/api/courses/<id>
    Expected: 200 and the course object

    Update the course (PUT)

    curl -s -X PUT -H "Content-Type: application/json"
    -d '{"status":"In Progress","name":"Intro to Python (Updated)"}'
    http://localhost:5000/api/courses/<id>
    Expected: 200 and updated fields

    Delete the course (DELETE)

    curl -s -X DELETE http://localhost:5000/api/courses/<id>
    Expected: 204 and no content

    List after deletion

    curl -s -X GET http://localhost:5000/api/courses
    Expected: 200 and an array without the deleted course

Error scenarios (copy-paste): A) POST missing required field (name)

    curl -s -X POST -H "Content-Type: application/json"
    -d '{"description":"Missing name field","target_completion_date":"2026-06-01","status":"Not Started"}'
    http://localhost:5000/api/courses
    Expected: 400 with an error message

B) POST invalid date

    curl -s -X POST -H "Content-Type: application/json"
    -d '{"name":"Bad Date","description":"Invalid date","target_completion_date":"2026-02-30","status":"Not Started"}'
    http://localhost:5000/api/courses
    Expected: 400 with a date format error

C) POST invalid status

    curl -s -X POST -H "Content-Type: application/json"
    -d '{"name":"Bad Status","description":"Bad status","target_completion_date":"2026-09-01","status":"Starting"}'
    http://localhost:5000/api/courses
    Expected: 400 with a status validation error

D) GET non-existent course

    curl -s -X GET http://localhost:5000/api/courses/non-existent-id
    Expected: 404

E) PUT non-existent course

    curl -s -X PUT -H "Content-Type: application/json"
    -d '{"status":"Completed"}' http://localhost:5000/api/courses/non-existent-id
    Expected: 404

F) PUT invalid date

    curl -s -X PUT -H "Content-Type: application/json"
    -d '{"target_completion_date":"2026-02-30"}' http://localhost:5000/api/courses/<id>
    Expected: 400

G) PUT invalid status

    curl -s -X PUT -H "Content-Type: application/json"
    -d '{"status":"Unknown"}' http://localhost:5000/api/courses/<id>
    Expected: 400

H) DELETE non-existent

    curl -s -X DELETE http://localhost:5000/api/courses/non-existent-id
    Expected: 404

I) Invalid JSON payload (malformed)

    curl -s -X POST -H "Content-Type: application/json"
    -d '{"name":"Bad JSON","description":"Missing closing brace" ' http://localhost:5000/api/courses
    Expected: 400 (error about bad JSON)

J) Missing Content-Type

    curl -s -X POST -d '{"name":"No content-type","description":"Should fail"}' http://localhost:5000/api/courses
    Expected: 400

Payload examples (reuse in tests)

A) POST valid with explicit status { "name": "Intro to Python", "description": "Learn Python basics", "target_completion_date": "2026-12-31", "status": "Not Started" }

B) POST valid without status (default) { "name": "Git Essentials", "description": "Learn Git commands", "target_completion_date": "2026-05-01" }

C) PUT update multiple fields { "name": "Intro to Python (Updated)", "description": "Updated description", "target_completion_date": "2027-01-15", "status": "In Progress" }

D) PUT partial update { "status": "Completed" }

Tips

    For happy paths, you should see 200/201 responses with the created or updated course object.
    For errors, you’ll see 400 or 404 with a JSON error message explaining the issue.

If you’d like, I can convert these into a small shell script to run an end-to-end test flow automatically.
7) Troubleshooting common issues

    Server won’t start (port in use)
        Check which process is using port 5000 and stop it, or run on a different port.
        Quick test: try running with a different port by modifying app.py to app.run(port=5001) or using Flask CLI with env var.

    Python or Flask not found
        Ensure you activated your virtual environment (see installation steps).
        Ensure Python is in your PATH.

    JSON storage file errors
        If data/courses.json is corrupted, the app may fail to parse JSON.
        Fix: reset to [] (empty list) for a clean start:
            echo [] > data/courses.json
        Ensure data/ directory exists and is writable.

    Permissions errors writing to data/courses.json
        Check file system permissions and run with appropriate rights.

    Validation errors (date or status)
        Ensure target_completion_date is in YYYY-MM-DD format.
        Ensure status is one of: Not Started, In Progress, Completed.

    Unexpected 404 on valid IDs
        Make sure you’re using the correct id from a previous POST response.
        IDs are UUIDs generated by the server.

8) Project structure explanation

CodeCraftHub/

    app.py
        The main Flask application. Defines routes for:
            GET /courses
            GET /courses/<id>
            POST /courses
            PUT /courses/<id>
            DELETE /courses/<id>
        Includes data validation helpers (date format, status validation) and JSON file read/write helpers.
    requirements.txt
        Python dependencies (Flask). Example: Flask>=2.0
    data/
        courses.json
            JSON file that stores an array of course objects.
            On first run, this can be an empty list: []
    README.md
        This file. It explains how to use CodeCraftHub, how to install, run, and test.

Notes for learners

    This project is intentionally simple to help you learn REST concepts without databases.
    Think of data/courses.json as a tiny database for learning purposes.
    You can extend this in many ways later (search, filtering, pagination, validation helpers, or moving to a real database).
