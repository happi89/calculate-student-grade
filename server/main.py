from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://grading-system-python-hw.vercel.app/?",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3001/?",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def calculate_student(name, mark, courseCode):
    aboveAchievment = ' You are above provincial standard'
    belowAchievment = ' You are below provincial standard'
    returnStatment = {"name": name, 'code': courseCode,'mark': mark}

    if(mark >= 95 and mark <= 100):
        return returnStatment, aboveAchievment, ' and your grade is 4+'
    elif(mark >= 87 and mark <= 94):
        return returnStatment, aboveAchievment, ' and your grade is 4'
    elif(mark >= 80 and mark <= 96):
        return returnStatment, aboveAchievment, ' and your grade is 4-'
    elif(mark >= 77 and mark <= 79):
        return returnStatment, aboveAchievment, ' and your grade is 3+'
    elif(mark >= 73 and mark <= 76):
        return returnStatment, aboveAchievment, ' and your grade is 3'
    elif(mark >= 70 and mark <= 72):
        return returnStatment, aboveAchievment, ' and your grade is 3-'
    elif(mark >= 67 and mark <= 69):
        return returnStatment, belowAchievment, ' and your grade is 2+'
    elif(mark >= 63 and mark <= 66):
        return returnStatment, belowAchievment, ' and your grade is 2'
    elif(mark >= 60 and mark <= 62):
        return returnStatment, belowAchievment, ' and your grade is 2-'
    elif(mark >= 50 and mark <= 59):
        return returnStatment, belowAchievment, ' and your grade is 1'
    elif(mark < 50):
        return returnStatment, belowAchievment, ' and your grade is 0'
    else:
        return 'invalid input'

@app.post("/")
async def calculate_grade(name: str, mark: int, code: str):
    result = calculate_student(name, mark, code)
    return { "result": result }
