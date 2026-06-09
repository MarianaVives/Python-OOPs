import datetime as dt
import os
import smtplib
import random

file_path = os.path.join("utils", "verses.txt")
current_dir = os.getcwd()
verses_txt = os.path.join(current_dir, file_path)

my_email = "automationqatesting65@gmail.com"
password = "mvyq lcah icwj tpbz"
to_email = "automationqatesting65@yahoo.com"
verses=[]
my_verse=""

try:
    with open(verses_txt, encoding='utf-8', errors='ignore') as file:
        verses=[verse for verse in file.readlines()]
except FileNotFoundError:
    print("No verses file found")
else:
    print("ok")

def get_time():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    return day_of_week

def automated_email_sent():
    if get_time() == 1:
        print(select_verse())
        send_email()


def select_verse():
    global my_verse
    my_verse = random.choice(verses)
    return my_verse

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:  # email provider @gmail com | smtp.mail.yahoo.com
        connection.starttls()  # Transport Layer Security - encrypt messages
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:Your Weekly Verse\n\n \nHere is your weekly Verse. \n \nRead the following Bible verse to enlighten your day:"
                                f"\n \n{select_verse()}\n Regards, \n QA Testing Automation")


automated_email_sent()