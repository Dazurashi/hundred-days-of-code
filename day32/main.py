'''
This program sends happy birthday email to people automatically if it's their birthday
'''

import smtplib
import datetime as dt
import pandas as pd
import random

my_email = "youremailhere"
password = "yourpasswordhere"

today = (dt.datetime.now().month, dt.datetime.now().day)


data = pd.read_csv("birthdays.csv")
bd_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
print(bd_dict)

if today in bd_dict:
    person = bd_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])
        print(contents)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")