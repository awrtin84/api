from fastapi import FastAPI
from pydantic import BaseModel




app = FastAPI()

class student(BaseModel):
    day : str
    month : str
    year : str
@app.post("/")

def check_name(student):
    day = student.day
    month = student.month
    year = student.year
    if len(day) == 2 and len(month) == 2:
        day = int(day)
        month = int(month)
        year = int(year)
        if 1339 < year < 1385 :
            if 0 < month <= 6 :
                if 0 < day < 32 :
                    return F"!تاریخ تولد شما با موفقیت ثبت گردید"
                else :
                    return F"!روز وارد شده خارج از مقادیر ممکن است ، روز تولد باتوجه به ماه تولد عددی بین 1 تا 31 می باشد"
            elif 6 < month < 12 :
                if 0 < day < 31:
                    return F"!تاریخ تولد شما با موفقیت ثبت گردید"
                else :
                    return F"!روز وارد شده خارج از مقادیر ممکن است ، روز تولد باتوجه به ماه تولد عددی بین 1 تا 30 می باشد"
            elif month == 12 :
                if 0 < day < 30 :
                    return F"تاریخ تولد شما با موفقیت ثبت گردید"
                else :
                    return F"!روز وارد شده خارج از مقادیر ممکن است ، روز تولد با توجه به ماه تولد عددی بین 1 تا 29  می باشد"
            else :
                return F"!ماه وارد شده خارج از مقادیر ممکن است، مقدار ماه باید عددی بین 1 تا 12 باشد"
        return F"!سال وارد شده باید به صورت عددی 4 رقمی بین 1339 تا 1385 باشد"
    return F"!روز و ماه باید عددی دو رقمی باشند ، مثلا برای ثبت عدد 1 باید بصورت 01 ثبت گردد"