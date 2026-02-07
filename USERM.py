from flask import Flask, render_template, request, jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['To'] = to
    
    user = "dummy@gmail.com"
    msg['From'] = user
    password = "your_app_password"  
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    message = data.get('message')
    if message:
        email_alert("Assistive Alert", message, "sank6@gmail.com")
        return jsonify({"status": "success", "message": "Email sent successfully"})
    return jsonify({"status": "error", "message": "No message provided"})

if __name__ == "__main__":
    app.run(debug=True)
