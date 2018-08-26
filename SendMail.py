import smtplib

sender = "kievbsm@gmail.com"
recipient = "Sergey.Glinyanskiy@gmail.com"
password = "IbeeD1_BSMBIN1"  # Your SMTP password for Gmail
subject = "Test email from Python"
text = "Hello from Python\nThis is line 2\nAnd line 3"

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login(sender, password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.close()
