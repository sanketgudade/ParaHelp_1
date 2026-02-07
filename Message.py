import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to
    
    user = "Dummy@gmail.com"
    msg['From'] = user
    password = "123"  
    
    server = smtplib.SMTP("smtp.gmail.com", 58)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()

if __name__ == "__main__":
    email_alert("hey", "hello sanket this messege is from PARAHELP", "sanketgudade006@gmail.com")
