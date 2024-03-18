from fastapi import FastAPI

app = FastAPI()

@app.get("/{student_id}")

def check(student_id):
    L = len(student_id)
    student_id = int(student_id)
    if L == 11:
        year = student_id // 100000000
        if 400 <=year <= 402:
            sabet = (student_id // 100) - (year * 1000000)
            if sabet == 114150:
                last = student_id % 100
                if 1 <= last <= 99 :
                     return F"!شماره دانشجویی درست می باشد" , student_id
                return F"!قسمت اندیس نادرست می باشد"
            return F"!قسمت ثابت نادرست می باشد"
        return F"!قسمت سال نادرست می باشد"
    return F"!شماره دانشجویی باید 11 رقم باشد "
