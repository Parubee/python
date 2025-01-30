from datetime import datetime
def calc_age(birthdate):
    today=datetime.today()
    age = today.year - birthdate.year

    if (today.month,today.day)<(birthdate.month,birthdate.day):
        age -=1
    return age
    
birthdate_str = input("Enter your birthdate(YYYY:MM:DD) :")

try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        age = calc_age(birthdate)
        print(f"Your age is :{age} years")
except ValueError:
        print("Invaild date format....Please use YYYY-MM-DD.")    

