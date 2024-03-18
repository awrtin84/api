from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI()
class student(BaseModel):
    address : str

@app.post("/")

def check_city(student):
    address = student.address
    if len(address) > 0 :
        if len(address) > 100 :
            return F'آدرس شما ثبت گردید'
        return F'حداکثر مقادیر ممکن برای این فیلد 100 کاراکتر است'
    return F'!فیلد آدرس نمیتوان خالی باشد'