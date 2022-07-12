import smtplib

SENDER_EMAIL_ADDRESS = 'sender@gmail.com'
RECEIVER_EMAIL_ADDRESS = 'receiver@gmail.com'
EMAIL_PASSWORD = 'password'
USER_NAME = 'user'
with smtplib.SMTP('valid-dns-name', 25) as smtp:
    print("Initiating mail request")

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(USER_NAME, EMAIL_PASSWORD)

    subject = 'Test Mail using smtplib with new DNS'
    body = "Hello All, \nThis is test mail from stmplib sample" \
           "\n\n\n Best Regards\nDev Team"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, msg)

    print("Successfully sent mail")
