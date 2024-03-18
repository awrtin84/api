from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class student(BaseModel):
    phone_number : str

@app.post("/")

def check(student):
    phone_number = student.phone_number
    if len(phone_number) == 11 and phone_number.isdigit() == True:
        if int(phone_number[0]) == 0:
             return F'!شماره تلفن شما با موفقیت ثبت گردید'
        return F'!شماره تلفن وارد شده باید با 09 شروع شود'
    return F"!شماره تلفن عددی یازده رقمی است، لطفا در وارد کردن رقمها دقت فرمایید"
