from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class student(BaseModel):
    f_name : str
    l_name :str

@app.post("/")

def check_name(student):
    f_name = student.f_name
    l_name = student.l_name
    if len(f_name) <= 10 and len(l_name) <=10 :
        if len(f_name) == 0 or len(l_name) == 0:
            return "!لظفا نامها را ارسال کنید . هیچ کادری نمیتواند خالی باشد"
        if f_name.isalpha() == True and l_name.isalpha() == True :
            for n in f_name :
                if ord(n)>122 :
                    for m in l_name:
                        if ord(m)>122:
                             return F'!نام شما تایید شد'
                        return F'!نام خانوادگی را به حروف فارسی وارد کنید'
                return F'!نام شما باید با حروف فارسی مشخص شود'
        return F'!نام نباید شامل علاعم یا حروف باشد'
    return F'!حداکثر کاراکتر مجاز برای نام 10 کاراکتر به اضای هر مقدار ارسالی است'
