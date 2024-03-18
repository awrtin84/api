from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class student(BaseModel):
    city : str

iran_provinces = {
    "آذربایجان شرقی": "تبریز",
    "آذربایجان غربی": "ارومیه",
    "اردبیل": "اردبیل",
    "اصفهان": "اصفهان",
    "البرز": "کرج",
    "ایلام": "ایلام",
    "بوشهر": "بوشهر",
    "تهران": "تهران",
    "چهارمحال و بختیاری": "شهرکرد",
    "خراسان جنوبی": "بیرجند",
    "خراسان رضوی": "مشهد",
    "خراسان شمالی": "بجنورد",
    "خوزستان": "اهواز",
    "زنجان": "زنجان",
    "سمنان": "سمنان",
    "سیستان و بلوچستان": "زاهدان",
    "فارس": "شیراز",
    "قزوین": "قزوین",
    "قم": "قم",
    "کردستان": "سنندج",
    "کرمان": "کرمان",
    "کرمانشاه": "کرمانشاه",
    "کهگیلویه و بویراحمد": "یاسوج",
    "گلستان": "گرگان",
    "گیلان": "رشت",
    "لرستان": "خرم‌آباد",
    "مازندران": "ساری",
    "مرکزی": "اراک",
    "هرمزگان": "بندرعباس",
    "همدان": "همدان",
    "یزد": "یزد"
}

@app.post("/")

def check_city(student):
    city = student.city
    if len(city) > 0 :
        for i in city :
            if ord(i) > 122 :
                provinces_list = list(iran_provinces.values())
                if city in provinces_list:
                    return F"!استان شما با موفقیت ثبت گردید"
                else:
                    return F"!شهر شما باید مرکز یکی از استانها باشد"
            return F"!نام استان باید فارسی باشد"
    return F"!فیلد استان نباید خالی باشد"