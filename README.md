# Edutrack_app

A simple FastAPI-based REST API for managing users, courses, and enrollments — built with clean architecture, in-memory data storage, and Pydantic schemas.

This project demonstrates how to structure a modular FastAPI backend with routers, services, and schemas while maintaining testability and scalability.

🚀 Features

👥 User Management

Create, update, delete, and deactivate users

🎓 Course Management

Create, update, delete, and deactivate courses

📝 Enrollments

Enroll users in courses

Mark course completion

View user enrollments

List users enrolled in specific courses

✅ In-memory data persistence for simplicity (using dictionaries)

🧪 Pytest test suite for all endpoints

🏗️ Project Structure
fastapi-course-enrollment/
│
├── main.py
├── database.py
│
├── routers/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
│
├── schemas/
│   ├── user.py
│   ├── course.py
│   ├── enrollment.py
│   └── response.py
│
├── services/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
│
├── tests/
│   ├── conftest.py
│   ├── test_user.py
│   ├── test_course.py
│   └── test_enrollment.py
│
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/fastapi-course-enrollment.git
cd fastapi-course-enrollment

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Server
uvicorn main:app --reload


Your API will be live at:
👉 http://127.0.0.1:8000

📚 API Documentation

FastAPI automatically generates Swagger UI and ReDoc docs.

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🔑 Example Endpoints
➕ Create a User

POST /users/create

{
  "name": "John Doe",
  "email": "john@example.com"
}


Response

{
  "success": true,
  "message": "User was successfully created",
  "data": {
    "id": "d52a7b5a-f4e2-4e32-9f63-9c4e61b6e2b3",
    "name": "John Doe",
    "email": "john@example.com",
    "is_active": true
  }
}

🎓 Create a Course

POST /courses/create

{
  "title": "Python Basics",
  "description": "Learn Python from scratch",
  "is_open": true
}

📝 Enroll a User

POST /enrollments/

{
  "user_id": "d52a7b5a-f4e2-4e32-9f63-9c4e61b6e2b3",
  "course_id": "7d13c58d-3a99-4574-a7d4-1b6d5f35b312"
}

🧪 Running Tests

Tests are written with pytest and use FastAPI’s TestClient.

Run all tests with:

pytest -v


✅ Tests cover:

User creation, deactivation, and deletion

Course creation and update

Enrollment creation, completion, and retrieval

🧱 Tech Stack
Layer	Technology
Framework	FastAPI
Schema Validation	Pydantic
Testing	Pytest
UUID Handling	Python uuid
In-memory Database	Python Dictionaries
🧩 Key Design Decisions

Modular architecture: Each resource (user, course, enrollment) has its own schema, router, and service layer.

In-memory DB: Simplifies testing and demonstration.

Typed responses: Every endpoint returns a unified Response schema.

UUID identifiers: Used consistently across all resources.

🤝 Contributing

Fork the repository

Create a new branch (feature/your-feature)

Commit your changes

Push your branch and open a PR

🧠 Author

Ifedolapo Ojo
🎓 Civil Engineering Graduate | 🐍 Python Developer | ✍️ Technical Writer
🔗 LinkedIn
 | GitHub

🪪 License

This project is licensed under the MIT License — see the LICENSE file for details.

This project is licensed under the MIT License — see the LICENSE
 file for details.
