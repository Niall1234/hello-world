import smtplib, pyinputplus

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
while True:
    password = pyinputplus.inputPassword("Enter password: ")
    try:
        smtpObj.login("robertniallross@gmail.com", password)
        break
    except Exception as err:
        print(err)
recipient = input("Enter recipient's email address: ")
subject = input("Enter subject: ")
body = input("Enter body: ")
smtpObj.sendmail("robertniallross@gmail.com", recipient, f"Subject: {subject}\n{body}")
smtpObj.quit()
