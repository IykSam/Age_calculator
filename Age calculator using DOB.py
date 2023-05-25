import datetime

def cal_age(year,month,day):
    today = datetime.date.today()
    dob = datetime.date(year,month,day)
    age = int((today-dob).days/365)
    return age

user_dob = input("Enter your D.O.B in this format 'Year-month-day' : ")
dob = user_dob.split('-')
year,month,day = int(dob[0]), int(dob[1]),int(dob[2])
your_age = cal_age(year,month,day)
print(f"You are {your_age} year old.")
