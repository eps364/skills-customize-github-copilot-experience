# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build and understand a small RESTful API using the FastAPI framework. You will practice defining endpoints, creating and validating data models with Pydantic, handling CRUD operations, and implementing error handling and query parameters. By the end, you should feel comfortable reading the interactive docs (Swagger UI) and extending the API.

## 📝 Tasks

### 🛠️ Project Setup & First Endpoint

#### Description
Initialize a FastAPI project and create a simple health/hello endpoint to confirm everything runs locally.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn (e.g. `pip install fastapi uvicorn`).
- Create an `app` instance of `FastAPI` in `main.py` or `starter-code.py`.
- Implement a `GET /` or `GET /health` endpoint returning a JSON message like `{"status": "ok"}`.
- Run the server locally (e.g. `uvicorn main:app --reload`) and view interactive docs at `/docs`.

### 🛠️ CRUD Endpoints with Pydantic Model

#### Description
Create a Pydantic model representing a resource (e.g. `Student`) and implement CRUD operations storing data in an in-memory list/dict.

#### Requirements
Completed program should:

- Define a `Student` model with fields: `id: int`, `name: str`, `grade: int` (0-100), `active: bool = True`.
- Implement endpoints:
  - `POST /students` (create) – validates body and returns created item.
  - `GET /students` (list) – returns all students.
  - `GET /students/{student_id}` – returns one student or 404.
  - `PUT /students/{student_id}` – updates an existing student fully.
  - `DELETE /students/{student_id}` – removes a student and returns 204 or a small JSON confirmation.
- Use proper HTTP status codes (201 for create, 404 for not found, 204 for delete).
- Validate that `grade` is between 0 and 100 (raise `HTTPException(status_code=422, ...)` if invalid).

### 🛠️ Query Parameters, Filtering & Error Handling

#### Description
Enhance the API with query filtering, partial updates, and improved error handling patterns.

#### Requirements
Completed program should:

- Add optional query params to `GET /students` (`min_grade`, `active`) to filter results.
- Implement a `PATCH /students/{student_id}` endpoint allowing partial updates (e.g. just `grade` or `active`).
- Return meaningful error messages (`{"detail": "Student not found"}`) using `HTTPException`.
- Add a custom exception handler for a made-up `NegativeGradeError` that returns status 400 if triggered.
- Include docstrings or comments explaining each endpoint.

---

### ✅ Stretch Ideas (Optional)
- Persist data to a JSON file or SQLite database.
- Add pagination to the list endpoint.
- Implement authentication stub (e.g. API key header check).

### 🧪 Example Usage Snippets
```bash
# Create a student
curl -X POST http://127.0.0.1:8000/students -H "Content-Type: application/json" -d '{"id":1,"name":"Alice","grade":95}'

# Get all students
curl http://127.0.0.1:8000/students

# Filter students
curl http://127.0.0.1:8000/students?min_grade=90&active=true
```

### 📚 Learning Goals
By completing this assignment you will be able to:
- Explain how FastAPI auto-generates OpenAPI docs.
- Build and test CRUD endpoints quickly.
- Use Pydantic models for validation and serialization.
- Handle errors with consistent JSON responses.

Good luck and have fun exploring FastAPI! 🚀
