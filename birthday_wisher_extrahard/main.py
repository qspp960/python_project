##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random


my_email = "smtptest960@gmail.com"
password = "huezptrtjmwjpdow"
# 1. Update the birthdays.csv
birthday_data = pd.read_csv('./birthdays.csv')
birthday_dict = birthday_data.to_dict(orient='records')


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

for birth in birthday_dict:
    if birth['month'] == month and birth['day'] == day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_number = random.randint(1,3)
        with open(f"./letter_templates/letter_{letter_number}.txt",'r') as letter:
            letter_data = letter.readlines()
            send_data = ""
            for d in letter_data:
                send_data += d.replace('[name]',birth['name']) + '\n'
# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=birth['email'],
                                    msg=f"Subject:hello\n\n {send_data}")



