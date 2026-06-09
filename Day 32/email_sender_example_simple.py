import smtplib
my_email = "automationqatesting65@gmail.com"
password = "mvyq lcah icwj tpbz"
to_email = "automationqatesting65@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as connection:#email provider @gmail com | smtp.mail.yahoo.com
    connection.starttls() #Transport Layer Security - encrypt messages
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg="Subject:Hello\n\nThis is the body of my email.")
