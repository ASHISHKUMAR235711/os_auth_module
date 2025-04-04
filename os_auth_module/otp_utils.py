import random
import smtplib
import ssl
from email.message import EmailMessage

# Generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send OTP to the user's email
def send_otp(email, otp):
    sender_email = "ashishkumar235711@gmail.com"
    sender_password = "iqvt nhea aeqv bubu"  # Use App Password, NOT real password

    msg = EmailMessage()
    msg.set_content(f"Your OTP is: {otp}")
    msg["Subject"] = "Your Verification OTP"
    msg["From"] = sender_email
    msg["To"] = email

    # Secure connection with Gmail's SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# OTP verification (compare input and sent otp)
def verify_otp(user_input, real_otp):
    return user_input == real_otp
