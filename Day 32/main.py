##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas as pd
import random

birthdays = 'birthdays.csv'
my_email = "lorenzomancinelli05@gmail.com"
password = 'akmogsybpoytfwkg'
letters = ['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt']
now = dt.datetime.now()
month = now.month
day = now.day
df = pd.read_csv(birthdays)

dict_of_bdays = df.to_dict(orient = 'records')

for entry in dict_of_bdays:
    if entry['month'] == month and entry['day'] == day:
        letter = random.choice(letters)
        send_to = entry['email']
        string = ''
        with open(letter) as file:
            list_lines = file.readlines()
            list_lines[0] = list_lines[0].replace('[NAME]', entry['name'])
        string = ''.join(list_lines)
        print(string)
        with smtplib.SMTP("smtp.gmail.com", port =587) as connection:
            connection.starttls()
            connection.login(user=  my_email, password = password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = send_to,
                msg = f'Subject:Happy BirthDay\n\n{string}'
            )