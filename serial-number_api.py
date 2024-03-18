from fastapi import FastAPI
from pydantic import BaseModel



class student(BaseModel):
    serial_number : str

app = FastAPI()

@app.post("/")

def validate_serial(student):
    serial = student.serial_number
    if len(serial) < 11:
        return f"حداقل میزان مجاز برای کاراکتر های این فیلد 11 عدد است"
    
    parts = serial.split('-')
    
    if len(parts) != 3:
        return F'!سریال شناسنامه باید دارای سه بخش باشد که با یک بک اسلش از هم جدا شده اند'
    
    if len(parts[0]) != 6: 
        return F'!بخش اول شماره سریال شناسنامه باید شیش رقم باشد'
    
    if not parts[0].isdigit():
        return F"!مقدار وارد شده در بخش اول باید تنه شامل عدد باشد"
    
    if len(parts[1]) != 1 or not parts[1].isalpha():
            return F'!بخش دوم باید شامل یک حرف فارسی باشد'
    if ord(parts[1]) < 400:
        return F'!بخش دوم باید شامل حرف فارسی باشد'
    if len(parts[2]) != 2 or not parts[2].isdigit():
        return F'!بخش سوم باید عددی دو رقمی باشد'
    else:
        return F'!سریال شناسنامه شما با موفقیت گردید '