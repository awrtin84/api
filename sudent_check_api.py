#چک کردن کد دانشجویی

def st_id(student_id):
    L = len(student_id)
    if L == 0 :
        return F"!فیلد شماره دانشجویی نمیتوان خالی باشد"
    if student_id.isdigit() == False:
        return F"!شماره دانشجویی باید بصورت عددی باشد"
    student_id = int(student_id)
    if L == 11:
        year = student_id // 100000000
        if 400<= year <=402:
            sabet = (student_id // 100) - (year * 1000000)
            if sabet == 114150:
                last = student_id % 100
                if 1 <= last <=100 :
                    return F"!شماره دانشجویی درست می باشد" , student_id
                return F"!قسمت اندیس نادرست می باشد"
            return F"!قسمت ثابت نادرست می باشد"
        return F"!قسمت سال نادرست می باشد"
    return F"!شماره دانشجویی باید 11 رقم باشد "



#چک کردن شهر و استان دانشجو

def city(city):
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




#چک کردن سریال شناسنامه


def serial_number(serial):
    if len(serial) == 0 :
        return F"!فیلد سریال شناسنامه خالی است . لطفا همه فیلدها را پر کنید"
    if len(serial) < 11:
        return F" !میزان مجاز برای کاراکتر های فیلد شماره سریال شناسنامه 11 عدد می باشد"
    
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




#چک کردن رشته تحصیلی دانشجو


def reshteh(reshteh):
    reshteha = {
    "مهندسی معدن" , "مهندسی برق" , "مهندسی عمران" , "حرفه و فن فرهنگیان" ,
      "مهندسی کامپیوتر" , "مهندسی شهرسازی" , "مهندسی مکانیک و پلیمر"
    }
    if len(reshteh) > 0 :
        for n in reshteh :
            if ord(n) > 122 :
                if reshteh in reshteha:
                    return F'!رشته شما با موفقیت ثبت گردید'
                else:
                    return F'!رشته انتخاب شده باید یکی از رشته های موجود باشد'
            return F'!نام رشته را به فارسی وارد کنید'
    return F'!فیلد رشته نباید خالی باشد'



#چک کردن نام دانشجو 


def name(f_name , l_name):
    if len(f_name) <= 10 and len(l_name) <=10 :
        if len(f_name) == 0 or len(l_name) == 0:
            return f"!لظفا نامها را ارسال کنید . هیچ کادری نباید خالی باشد"
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



#چک کردن کد ملی دانشجو


def code_meli(code_meli):
    l = len(code_meli)
    sum = 0
    if l == 0:
        return f'!فیلد کد ملی نمیتواند خالی باشد'
    if l == 10 :
        if code_meli.isdigit() == True :
            for i in range(0 , l - 1):
                c = ord(code_meli[i])
                c -= 48
                sum = sum + c *(l - i)
            r = sum % 11
            c = ord(code_meli[l - 1])
            c -= 48
            if r > 2:
                r = 11 - r
            if r == c:
                return F'!کد ملی شما با موفقیت ثبت گردید'
            else : 
                return F'!کد ملی وارد شده اشتباه است لطفا در وارد کردن ارقام دقت فرمایید'    
        return F'!کد ملی باید فقط شامل ارقام باشد'       
    return F'!میزان مجاز برای فیلد کد ملی 10 رقم است'



#چک کردن تاریخ تولد


def Birthday(day , month , year):
    if len(day) == 0 or len(month) == 0 or len(year) == 0 :
        return f'!هیچ یک از مقادیر سال و ماه و روز نمیتوان خالی باشند'
    if len(day) == 2 and len(month) == 2:
        day = int(day)
        month = int(month)
        year = int(year)
        if 1339 < year < 1385 :
            if 0 < month <= 6 :
                if 0 < day < 32 :
                    return F'!تاریخ تولد شما با موفقیت ثبت گردید'
                else :
                    return F"!روز وارد شده خارج از مقادیر ممکن است ، روز تولد باتوجه به ماه تولد عددی بین 1 تا 31 می باشد"
            elif 6 < month < 12 :
                if 0 < day < 31:
                    return F"!تاریخ تولد شما با موفقیت ثبت گردید"
                else :
                    return F"!روز وارد شده خارج از مقادیر ممکن است ، روز تولد باتوجه به ماه تولد عددی بین 1 تا 30 می باشد"
            elif month == 12 :
                if 0 < day < 30 :
                    return F"!تاریخ تولد شما با موفقیت ثبت گردید"
                else :
                    return F"!روز وارد شده خارج از مقادیر ممکن است ، روز تولد با توجه به ماه تولد عددی بین 1 تا 29  می باشد"
            else :
                return F"!ماه وارد شده خارج از مقادیر ممکن است، مقدار ماه باید عددی بین 1 تا 12 باشد"
        return F"!سال وارد شده باید به صورت عددی 4 رقمی بین 1339 تا 1385 باشد"
    return F"!روز و ماه باید عددی دو رقمی باشند ، مثلا برای ثبت عدد 1 باید بصورت 01 ثبت گردد"



#چک کردن شماره تماس


def phone_number(phone_number):
    if len(phone_number) == 0 :
        return F"!لطفا فیلد شماره تلفن را پرکنید"
    if len(phone_number) == 11 and phone_number.isdigit() == True:
        if int(phone_number[0]) == 0 and int(phone_number[1]) == 9 :
            return F'!شماره تلفن شما با موفقیت ثبت گردید'
        return F'!شماره تلفن وارد شده باید با 09 شروع شود'
    return F"!شماره تلفن عددی یازده رقمی است، لطفا در وارد کردن رقمها دقت فرمایید"


#چک کردن شماره منزل

def home_phone_number(phone_number):
    if len(phone_number) == 0 :
        return F'لطفا فیلد شماره را پرکنید'
    if len(phone_number) == 11 and phone_number.isdigit() == True:
        if int(phone_number[0]) == 0:
            return F"!شماره تلفن شما با موفقیت گردید"
        return F"!شماره وارد شده باید با 0 شروع شود"
    return F"!شماره تلفن عددی یازده رقمی است لطفا در وارد کردن رقمها دقت فرمایید"


#چک کردن دانشکده


def daneshkadeh(daneshkadeh):
    daneshkadeha = {"فنی و مهندسی" , "علوم پایه"  , "علوم انسانی" , "دامپزشکی"  , "اقتصاد" "کشاورزی" , "منابع طبیعی"}
    if len(daneshkadeh) > 0 :
        for n in daneshkadeh :
            if ord(n) > 122 :
                if daneshkadeh in daneshkadeha:
                    return F"دانشکده شما با موفقیت ثبت گردید"
                else:
                    return F'!دانشکده انتخابی باید یکی از دانشکده های موجود باشد'
            return F"!نام دانشکده را به فارسی وارد کنید"
    return F"!فیلد دانشکده نباید خالی باشد"



#چک کردن آدرس


def address(address):
    if len(address) > 0 :
        if len(address) < 100 :
            return F"!آدرس شما ثبت گردید"
        return F"!حداکثر مقادیر ممکن برای این فیلد 100 کاراکتر است"
    return F"!فیلد آدرس نمیتوان خالی باشد"


#چک کردن کد پستی


def code_post(code_post):
    if len(code_post) == 10 and code_post.isdigit() == True:
        if int(code_post[0]) != 0 :
            return F'!کد پستی شما با موفقیت ثبت گردید'
        return F"!کد پستی نباید با صفر شروع بشود"
    return F"کد پستی عددی ده رقمی است لطفا در وارد کردن رقمها دقت فرمایید"