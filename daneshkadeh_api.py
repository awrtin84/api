from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class student(BaseModel):
    daneshkadeh : str

daneshkadeha = {"فنی و مهندسی" , "علوم پایه"  , "علوم انسانی" , "دامپزشکی"  , "اقتصاد" "کشاورزی" , "منابع طبیعی"}

@app.post("/")

def check_city(student):
    daneshkadeh = student.daneshkadeh

    if len(daneshkadeh) > 0 :
        for i in daneshkadeh :
            if ord(i) > 122 :
                if daneshkadeh in daneshkadeha:
                     return F"دانشکده شما با موفقیت ثبت گردید"
                else:
                    return F'!دانشکده انتخابی باید یکی از دانشکده های موجود باشد'
            return F"!نام دانشکده را به فارسی وارد کنید"
    return F"!فیلد دانشکده نباید خالی باشد"