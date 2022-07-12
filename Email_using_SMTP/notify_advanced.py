import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_PASSWORD = 'password'
USER_NAME = 'user'

print("Initiating mail request")

sender_email = 'sender@gmail.com'
receiver_emails = [
    'receiver1@gmail.com',
    'receiver2@gmail.com'
]

# Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "Test Mail with Attachment and HyperLink using smtplib"
msg["From"] = sender_email
msg["To"] = ", ".join(receiver_emails)
files = ['Dummy_Release_Data.txt']

# HTML Message Part
html = """\
<html>
  <head></head>
  <body>
    <p>Hello All, <br>
       Here is the
       <a href="https://google.com/">
       Google Link</a>
    </p>
    <div>Please find the attachment for Current Release Notes</div>
    <div>Best Regards,
    Dev Team
    </div>
  </body>
</html>
"""

part = MIMEText(html, "html")
msg.attach(part)

# Add Attachments
for file in files:
    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    # Set mail headers
    part.add_header(
        "Content-Disposition",
        "attachment", filename=file
    )
    msg.attach(part)

# Create SMTP connection and send email

with smtplib.SMTP('valid-dns-name', 25) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER_NAME, EMAIL_PASSWORD)

    server.send_message(msg)

print("Successfully sent mail")
