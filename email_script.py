import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_application(smtp_server, smtp_port, sender_email, password, recipient_email, subject, body, attachment_path):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = "sender_email"
    message["To"] = recipient_email
    message["Subject"] = subject

    # Replace the placeholder in the body with the company name
    body_with_company = body.replace("{company_name}", company_name)
    # Add body to the email
    message.attach(MIMEText(body_with_company, "plain"))

    # Attach the file
    with open(attachment_path, "rb") as file:
        attachment = MIMEApplication(file.read(), Name="attachment")
        attachment["Content-Disposition"] = f'attachment; filename="{attachment_path}"'
        message.attach(attachment)

    # Create a secure SSL/TLS connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to the email account
    server.login(sender_email, password)

    # Send the email
    server.send_message(message)

    # Clean up the connection
    server.quit()

# SMTP server details
smtp_server = "smtp.gmail.com"  # Replace with your SMTP server address
smtp_port = 587  # Replace with your SMTP server port

# Email content
subject = "Looking for Job"
body = "Sir/Mam,\nGood Afternoon\n\nI hope this email finds you well. I would be thrilled to have the opportunity to contribute to {company_name}'s success. Thank you for considering my application. I am available at your convenience for any further discussion. \n\nRegards"

# File containing email addresses
email_list_file = "email_list.txt"

# File attachment
attachment_path = "resume.pdf"  # Replace with the path to your attachment file

#Read credentials
with open("credentials.txt", "r") as credentials_file:
    lines = credentials_file.read().splitlines()
    sender_email = lines[0]
    password = lines[1]


# Read email addresses and company names from file and send applications
with open(email_list_file, "r") as file:
    lines = file.read().splitlines()
    email_addresses = lines[::2]  # Every other line is an email address
    company_names = lines[1::2]  # Every other line is a company name


for recipient_email, company_name in zip(email_addresses, company_names):
    # Send the job application to each recipient
    send_application(smtp_server, smtp_port, sender_email, password, recipient_email, subject, body, attachment_path)
