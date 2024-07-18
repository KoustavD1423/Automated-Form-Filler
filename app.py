from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'koustavsamurai410@gmail.com'
app.config['MAIL_PASSWORD'] = 'generated_password' #didnt add for security reasons
app.config['MAIL_DEFAULT_SENDER'] = 'koustavsamurai410@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    
    screenshot_path = 'C:\\Users\\koust\\Downloads\\tasks\\static\\confirmation_page.png'
    resume_path = 'C:\\Users\\koust\\Downloads\\tasks\\static\\Koustav_Das_New_Resume1.pdf'
    Documentation_path = 'C:\\Users\\koust\\Downloads\\tasks\\static\\DOCUMENTATION_OF_APPROACH.pdf'

    
    subject = 'Python (Selenium) Assignment - Koustav Das'
    body = '''
    1. Screenshot of the form filled via code- already attached.
    2. Source code: https://github.com/KoustavD1423/Automated-Form-Filler.git
    3. Brief documentation of my approach already attached.
    4. My resume- already attached.
    5. Links to past projects/work samples:
        - Melody-Motion: https://github.com/KoustavD1423/Melody-Motion-main.git
        - Verdant-Vision: https://github.com/KoustavD1423/VerdantVision.git
        - GAN-Anime-Artify: https://github.com/KoustavD1423/GAN-Anime-Artify.git
        - Guardian-Gaze: https://github.com/KoustavD1423/Guardian-Gaze.git
    6. Yes i am availab to work full time (10 am to 7 pm) for the next 3-6 months.
    '''
    to_emails = ['tech@themedius.ai']
    cc_emails = ['hr@themedius.ai']

    msg = Message(subject, recipients=to_emails, cc=cc_emails, body=body)
    msg.attach('confirmation_page.png', 'image/png', open(screenshot_path, 'rb').read())
    msg.attach('Koustav_Das_New_Resume1.pdf', 'application/pdf', open(resume_path, 'rb').read())
    msg.attach('DOCUMENTATION_OF_APPROACH.pdf', 'application/pdf', open(Documentation_path, 'rb').read())

    mail.send(msg)

    return 'Email sent successfully.'

if __name__ == '__main__':
    app.run(debug=True)
