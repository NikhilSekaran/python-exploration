import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Initiating mail request")

# Create a text/plain message

Text = "Hello All, \nThis is test mail from stmplib sample" \
       "\n\n\n Best Regards\nDev Team"
html = """\
<html>
  <head></head>
  <body>
    <p>Hello All, <br>
       Here is the
       <a href="https://google.com/">
       Google Link</a>
    </p>
  </body>
</html>
"""
# msg = MIMEMultipart(html, _subtype='html')
msg = EmailMessage()
msg.set_content(Text)

files = ['Dummy_Release_Data.txt']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application',
                       subtype='octet-stream', filename=file_name)

msg['Subject'] = "Test Mail using smtplib"
msg['From'] = 'sender@gmail.com'
recipients = ['receiver@gmail.com']
msg['To'] = ", ".join(recipients)
# Send the message via our own SMTP server.
s = smtplib.SMTP('valid-dns-to-be-used', 25)
s.send_message(msg)
s.quit()

print("Successfully sent mail")
