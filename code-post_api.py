from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class student(BaseModel):
    code_post : str

@app.post("/")

def check(student):
    code_post = student.code_posty
    if len(code_post) == 10 and code_post.isdigit() == True:
        if int(code_post[0]) != 0 :
               return F'!کد پستی شما با موفقیت ثبت گردید'
        return F"!کد پستی نباید با صفر شروع بشود"
    return F"کد پستی عددی ده رقمی است لطفا در وارد کردن رقمها دقت فرمایید"