# import smtplib
#
# my_email = "chukwuemekalearning@gmail.com"
# password = "xznskpnfqgcgfqfg" # Special app password for this app.
#
# with smtplib.SMTP("smtp.gmail.com", 587,
#                           timeout=120) as connection:
#     connection.starttls() # TLS: Transport Layer Security.
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="chukwuemekangumoha@gmail.com",
#                         # The '\n\n' seperates subject from body.
#                         msg="Subject:Hello\n\nHi There, Having a great day ?")
#     # connection.close() # No longer needed because of 'with'

# """WORKING WITH datetime MODULE"""
# import datetime as dt
#
# now = dt.datetime.now() # Today's date & time in local timezone.
# print(type(now))
# print(type(now.year))

"""MINIPROJECT: Send email to myself on Thursday."""
import csv
import datetime as dt
import random
import smtplib
now = dt.datetime.now()

my_email = "chukwuemekalearning@gmail.com"
password = "xznskpnfqgcgfqfg"

# If today is a Thursday
if now.weekday() == 3:
    with open("Quotes.csv", mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        line = random.choice(list(reader))
        quote = line[0]
        author = line[1]
        # Send email
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr=my_email,
                          to_addrs="chukwuemekangumoha@proton.me",
                          msg="Subject:Thursday Motivation\n\n"
                          f"{quote}\n\t\t{author}")