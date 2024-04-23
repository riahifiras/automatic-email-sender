import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, message_body, attachment_path):
    # Set up the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach message body
    msg.attach(MIMEText(message_body, 'plain'))

    # Attach PDF file
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )
    msg.attach(part)

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Read email addresses from the text file
with open("email_list.txt", "r") as file:
    emails = file.read().splitlines()

# Set up sender email credentials
sender_email = ""
sender_password = ""  # foolow the steps in the readme to know hot to get this password (not email password !!!!
subject = "Subject of the email"
message_body = "Body of the email"
attachment_path = "aa.pdf" # pdf to attach

# Iterate through the list of emails and send email to each
for email in emails:
    send_email(sender_email, sender_password, email, subject, message_body, attachment_path)

print("Emails sent successfully.")
