from fastapi import FastAPI
from pydantic import BaseModel
import sudent_check_api 


class student(BaseModel):
    student_id : str
    f_name : str
    l_name :str
    code_meli : str
    serial_number : str
    year : str
    month : str
    day : str
    phone_number : str
    home_phone_number : str
    daneshkadeh : str
    reshteh : str
    state : str
    city : str
    address : str
    code_post : str

app = FastAPI()

@app.post("/")

def check_all(student):
    return sudent_check_api.student_id(student.student_id) , sudent_check_api.name(student.f_name , student.l_name) , sudent_check_api.code_meli(student.code_meli) ,sudent_check_api.serial_number(student.serial_number) ,  sudent_check_api.Birthday(student.day , student.month , student.year) ,sudent_check_api.phone_number(student.phone_number) ,sudent_check_api.home_phone_number(student.home_phone_number) , sudent_check_api.daneshkadeh(student.daneshkadeh) ,  sudent_check_api.reshteh(student.reshteh) ,  sudent_check_api.city(student.state) ,sudent_check_api.city(student.city) , sudent_check_api.address(student.address) , sudent_check_api.code_posty(student.code_post)