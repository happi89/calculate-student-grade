from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

def calculate_student(name, mark, courseCode):
    aboveAchievment = ' You are above provincial standard'
    belowAchievment = ' You are below provincial standard'
    returnStatment = print('name:', name, '\n', 'course code:', courseCode, '\n','mark:', mark)

    if(mark >= 95 and mark <= 100):
        print(returnStatment, '\n', aboveAchievment, ' and your grade is 4+')
    elif(mark >= 87 and mark <= 94):
        print(returnStatment, '\n', aboveAchievment, ' and your grade is 4')
    elif(mark >= 80 and mark <= 96):
        print(returnStatment, '\n', aboveAchievment, ' and your grade is 4-')
    elif(mark >= 77 and mark <= 79):
        print(returnStatment, '\n', aboveAchievment, ' and your grade is 3+')
    elif(mark >= 73 and mark <= 76):
        print(returnStatment, '\n', aboveAchievment, ' and your grade is 3')
    elif(mark >= 70 and mark <= 72):
        print(returnStatment, '\n', aboveAchievment, ' and your grade is 3-')
    elif(mark >= 67 and mark <= 69):
        print(returnStatment, '\n', belowAchievment, ' and your grade is 2+')
    elif(mark >= 63 and mark <= 66):
        print(returnStatment, '\n', belowAchievment, ' and your grade is 2')
    elif(mark >= 60 and mark <= 62):
        print(returnStatment, '\n', belowAchievment, ' and your grade is 2-')
    elif(mark >= 50 and mark <= 59):
        print(returnStatment, '\n', belowAchievment, ' and your grade is 1')
    elif(mark < 50):
        print(returnStatment, '\n', belowAchievment, ' and your grade is 0')
    else:
        print('invalid input')

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}
