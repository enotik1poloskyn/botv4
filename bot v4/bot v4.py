import sqlite3
import calendar
import datetime
import start_defs as start
conn = sqlite3.connect("user_fin.db") 
cur = conn.cursor()
def counter(type1,salary,expense,percent,days):
    if type1 == "day":
        return round(((salary - expense)- salary*percent)/days )
    elif type1 == "month":
        return salary*percent
    else:
        return (salary*percent)*12
def check_salary(salary,expense):
    if salary <= expense or salary == 0 :
        return False
    else:
        return True
def check_percent (salary,expense,percent):
    if percent >= 1:
            percent *= 0.01
    if salary - (salary*percent) < expense:
        return False
    else:
        return True
def days ():
    answer_1 = input("Date of income(YYYY-MM-DD): ")
    answer_2 = input("Date of your next income(YYYY-MM-DD):")
    format_1 = answer_1.split('-')
    format_2 = answer_2.split('-')
    try:
        transfom_1 = datetime.date(int(format_1[0]),int(format_1[1]),int(format_1[2]))
        transfom_2 = datetime.date(int(format_2[0]),int(format_2[1]),int(format_2[2]))
        return str(transfom_2 - transfom_1).split()[0]
    except:
        print("Incorrect format.")
        return False
def new_user (userid):
    cur.execute("CREATE TABLE IF NOT EXISTS User_Info_%s(reg INTEGER,salary INTEGER,expense INTEGER ,percent FLOAT, spend_day INTEGER,month INTEGER, year INTEGER,days INTEGER)"%userid)
    cur.execute("CREATE TABLE IF NOT EXISTS Days_%s (date TEXT, daily_expense TEXT,cost INTEGER,remains INTEGER )"%userid)
    cur.execute("INSERT INTO User_Info_%s VALUES(0,0,0,0,0,0,0,0)"%userid)
    cur.execute("INSERT INTO Days_%s VALUES(0,0,0,0)"%userid)
def update_info (userid,type_data,value):
    cur.execute("UPDATE User_Info_%s SET %s = %d "%(userid,type_data,value))


start_1 = start.ask()
if start_1 == True :
    userid = start.unic_id()
    new_user(userid)
else:
    userid = start.check_user()



cur.execute("SELECT reg FROM User_info_%s ORDER BY reg LIMIT 1"%userid)
a = cur.fetchone()[0]
if a == 0:
    salary = 0
    expense  = 0
    percent_1 = 1
    while check_salary(salary,expense) == False:
        salary = int(input("Enter your salary :"))
        expense = int(input("Enter your expense :"))
    percent = int(input("Enter your percent :"))
    while check_percent(salary,expense,percent) == False:
        print ("Error, you can`t use this percent.")
        percent = input("Try again:")
        print(percent)
    percent_1 = float(percent)
    if percent >= 1:
            percent_1 = percent * 0.01
    days_1 = days()
    while days_1 == False:
       days_1 = days()   
    days = int(days_1)
    
    update_info(userid,"reg",1)
    update_info(userid,"salary",salary)
    update_info(userid,"expense",expense)
    update_info(userid,"percent",percent)
    update_info(userid,"spend_day",counter("day",salary,expense,percent_1,days))
    update_info(userid,"month",counter("month",salary,expense,percent_1,days))
    update_info(userid,"year",counter("year",salary,expense,percent_1,days))
    update_info(userid,"days",days)
    conn.commit()






conn.commit()
cur.close()
conn.close()