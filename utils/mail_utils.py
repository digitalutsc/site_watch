"""
csv_utils.py - A collection of functions for sending emails.

This module contains logic for sending a generic email from a particular email to a list of recipients.
It also contains logic specific to SiteWatch for sending out emails to users when tests fail or errors occur in the checks.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from colorama import Fore


def send_email(sender_email: str, sender_name: str, recipient_emails: list, subject: str, body: str, attachment_paths: list = []) -> bool:
    """ Send an email from <sender_email> to <recipient_emails> with the given <subject> and <body> and optional
    attachments located at <attachment_paths>."""
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
        print(Fore.RED, f"An error occurred while sending the email: {e}", Fore.RESET)
        return False


def send_test_failure_email(config: dict, output_csv_name: str, output_log_name: str):
    """ Send an email to the recipients listed in the config file containing the output CSV and log files."""
    sender_email = config['email']['sender_email']
    sender_name = config['email']['sender_name']
    recipient_emails = config['email']['recipient_emails']
    subject = "SiteWatch Error Report"
    body = "One or more erros have been detected in the most recent run of SiteWatch. Please check the attached CSV and log files for more information."
    attachments = [output_csv_name, output_log_name]
    send_email(sender_email, sender_name, recipient_emails, subject, body, attachments)
    print(Fore.GREEN, "An email has been sent to the recipients listed in the config file as errors have been detected.")


def send_invalid_csv_email(config: dict, output_log_name: str):
    """ Send an email to the recipients listed in the config file containing the log file."""
    sender_email = config['email']['sender_email']
    sender_name = config['email']['sender_name']
    recipient_emails = config['email']['recipient_emails']
    subject = "SiteWatch Error Report"
    body = "The CSV file provided is invalid. Please check the attached log file for more information."
    attachments = [output_log_name]
    send_email(sender_email, sender_name, recipient_emails, subject, body, attachments)
    print(Fore.GREEN, "An email has been sent to the recipients listed in the config file as the CSV file you provided is invalid.")
