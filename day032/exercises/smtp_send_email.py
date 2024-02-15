import os
import smtplib
from email.mime.text import MIMEText

# Never save credentials in GitHub
# they can get scraped if on a public repository, or they can be leaked on a private repository
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
to_email = os.getenv("TO_EMAIL")

text_subtype = 'plain'
content = "You have successfully received a 99 email!"
msg = MIMEText(content, text_subtype)
msg['Subject'] = "Udemy testing!"
msg['From'] = my_email


print("Start")
connection = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
print("TLS")
connection.starttls()
print("Login")
connection.login(user=my_email, password=my_password)
print("Sendmail")
connection.sendmail(from_addr=my_email, to_addrs=[to_email], msg=msg.as_string())

print("Close")
connection.close()
