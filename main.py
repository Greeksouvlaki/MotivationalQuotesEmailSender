# Description: This is a simple program that sends an email with a random quote from a file, only on Monday.
import datetime as dt
import smtplib
import random

my_email = "" #your email
password = "" #your password (use app password if you have 2FA enabled)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="jskou58@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")


