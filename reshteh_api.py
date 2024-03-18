from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

class student(BaseModel):
    reshteh : str
reshteha = {
    "مهندسی معدن" , "مهندسی برق" , "مهندسی عمران" , "حرفه و فن فرهنگیان" ,
      "مهندسی کامپیوتر" , "مهندسی شهرسازی" , "مهندسی مکانیک و پلیمر"
}

@app.post("/")

def check_reshte(student):
    reshteh= student.reshteh
    if len(reshteh) > 0 :
        for i in reshteh :
            if ord(i) > 122 :
                if reshteh in reshteha:
                    return F'!رشته شما با موفقیت ثبت گردید'
                else:
                    return F'!رشته انتخاب شده باید یکی از رشته های موجود باشد'
            return F'!نام رشته را به فارسی وارد کنید'
    return F'!فیلد رشته نباید خالی باشد'
