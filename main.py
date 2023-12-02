import fastapi
from student_data import students

app = fastapi.FastAPI()

# method for welcome message for the api at the root
@app.get("/")
async def welcome():
    return "Welcome to the student api"

# method to get all the student data
@app.get("/students")
async def get_students():
    return students

# method to get student data by student id
@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise fastapi.HTTPException(status_code=404, detail="student not found")

# uvicorn command to run the app on port 8000
# uvicorn main:app --reload --port 8000
# command to create requirements.txt file
# pip freeze > requirements.txt





