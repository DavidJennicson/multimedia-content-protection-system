import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def emailer(otp,rec,name):
    sender_email = "project.piapm@gmail.com"
    receiver_email = rec
    password = "pmicryqqpshpztzm"
    otp=str(otp)
    message = MIMEMultipart("alternative")
    message["Subject"] = "OTP Verification of Medcrypt"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    html = """\
    <html>
      <body>
        <h2>Hi """+name+""",<br>
           Your OTP is 
     </h2>
        <h1>"""+otp+"""</h1>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects

    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return True
