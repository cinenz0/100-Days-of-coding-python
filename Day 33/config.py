import smtplib
def send_mail():
    my_email = "lorenzomancinelli05@gmail.com"
    password = 'dqpmdtwrfijemkbj'
    send_to = "lorenzomancinelli09@gmail.com"
    with smtplib.SMTP("smtp.gmail.com" ,port = 587) as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = send_to,
            msg = f"Subject:lookup\n\nlook up"
        )