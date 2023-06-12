import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(sender_email: str, sender_name: str, recipient_emails: list, subject: str, body: str, attachment_paths: list=[]) -> bool:
    try:
        # Create a multipart message object
        message = MIMEMultipart()
        message["From"] = f"{sender_name} <{sender_email}>"
        message["To"] = ", ".join(recipient_emails)
        message["Subject"] = subject

        # Create the body of the email
        message.attach(MIMEText(body))

        # Attach files
        for attachment_path in attachment_paths:
            with open(attachment_path, "rb") as file:
                attachment = MIMEApplication(file.read())
                attachment.add_header("Content-Disposition", "attachment", filename=attachment_path)
                message.attach(attachment)

        # SMTP server details
        smtp_host = "localhost"
        smtp_port = 25

        # Send the email
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.send_message(message)

        return True

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        return False
