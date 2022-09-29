import smtplib
import datetime as dt
import random

my_email = "smtptest960@gmail.com"
password = "huezptrtjmwjpdow"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 3:

    with open("quotes.txt",'r') as quotes_data:
        all_quotes = quotes_data.readlines()
        today_quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="qspp@daum.net",
                            msg=f"Subject:hello\n\n {today_quote}")



