"""Starter code for FastAPI REST APIs assignment.

Run locally (after installing dependencies):
    uvicorn starter-code:app --reload

Then open: http://127.0.0.1:8000/docs for interactive Swagger UI.
"""
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Student API", description="Practice CRUD operations with FastAPI", version="0.1.0")

class Student(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    grade: int = Field(..., ge=0, le=100, description="Grade between 0 and 100")
    active: bool = True

# In-memory 'database'
students: List[Student] = []

@app.get("/health", summary="Health check")
def health() -> dict:
    return {"status": "ok"}

@app.post("/students", response_model=Student, status_code=201, summary="Create a student")
def create_student(student: Student) -> Student:
    # Prevent duplicate IDs
    if any(s.id == student.id for s in students):
        raise HTTPException(status_code=409, detail="Student with this ID already exists")
    students.append(student)
    return student

@app.get("/students", response_model=List[Student], summary="List students")
def list_students(min_grade: Optional[int] = None, active: Optional[bool] = None) -> List[Student]:
    result = students
    if min_grade is not None:
        result = [s for s in result if s.grade >= min_grade]
    if active is not None:
        result = [s for s in result if s.active == active]
    return result

@app.get("/students/{student_id}", response_model=Student, summary="Get single student")
def get_student(student_id: int) -> Student:
    for s in students:
        if s.id == student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}", response_model=Student, summary="Full update student")
def update_student(student_id: int, updated: Student) -> Student:
    for i, s in enumerate(students):
        if s.id == student_id:
            students[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/students/{student_id}", response_model=Student, summary="Partial update student")
def patch_student(student_id: int, name: Optional[str] = None, grade: Optional[int] = None, active: Optional[bool] = None) -> Student:
    for i, s in enumerate(students):
        if s.id == student_id:
            data = s.dict()
            if name is not None:
                data["name"] = name
            if grade is not None:
                if grade < 0 or grade > 100:
                    raise HTTPException(status_code=422, detail="Grade must be between 0 and 100")
                data["grade"] = grade
            if active is not None:
                data["active"] = active
            updated = Student(**data)
            students[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}", status_code=204, summary="Delete student")
def delete_student(student_id: int) -> None:
    for i, s in enumerate(students):
        if s.id == student_id:
            del students[i]
            return None
    raise HTTPException(status_code=404, detail="Student not found")

# Custom exception example (stretch goal)
class NegativeGradeError(Exception):
    pass

@app.exception_handler(NegativeGradeError)
def negative_grade_handler(_, __):
    return JSONResponse(status_code=400, content={"detail": "Grade cannot be negative"})

# NOTE: For the stretch goal you could raise NegativeGradeError somewhere if grade < 0 before Pydantic validation.
