import datetime as dt
import os
import smtplib
import random
import pandas as pd
import smtplib


my_email = "automationqatesting65@gmail.com"
password = "mvyq lcah icwj tpbz"
to_email = "automationqatesting65@yahoo.com"

file_path = os.path.join("utils", "birthdays.csv")
current_dir = os.getcwd()
bd_txt = os.path.join(current_dir, file_path)

SUBJECT ="HAPPY BIRTHDAY!"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

def email_config(subject,body):
    with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider @gmail com | smtp.mail.yahoo.com
        connection.starttls()  # Transport Layer Security - encrypt messages
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{body}")

try:
    data = pd.read_csv(bd_txt)
except FileNotFoundError:
    print("File not found")
else:
    #(12,24):Mariana, Mariana@live.com, 1234,02,01
    birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    random_num = random.randint(1,3)
    random_letter = f"utils/letter_{random_num}.txt"
    file_path_letter = os.path.join(current_dir,random_letter)
    try:
        with open (file_path_letter, "r") as file:
            letter_to_read = file.read()
            letter_to_read = letter_to_read.replace("[NAME]", birthday_person["name"])
            email_config(SUBJECT,letter_to_read)
    except FileNotFoundError:
        print("File not found.")


