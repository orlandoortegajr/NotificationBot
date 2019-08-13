import smtplib, ssl
from settings import email, email_password, receiver

"""
Handles setting up secure email connections with email provider gmail
Sends the email to the receiver using the application's gmail account
"""

#TODO: Allow user to also use hotmail/yahoo

def send_email(message_subject, message_text):
    """
    Send email to receiver through Gmail.

    Args:
        message_subject: subject of the email.
        message_text: content of the email.
    """
    port = 587 #Used for ssl

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        
        #login to server
        smtp.login(email, email_password)

        #message formatting
        msg = f'Subject: {message_subject}\n\n{message_text}'

        #send message
        smtp.sendmail(email, receiver, msg)



"""
Example of email text:

message = \"""\
Subject: Hi there

This message is sent from Python.\"""
"""

    