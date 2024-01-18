from flask import Flask 
from flask_mail import Mail, Message

app= Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'khabox52x@gmail.com'
app.config['MAIL_PASSWORD'] = 'vpha sdhj botu xujo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config['SECRET_KEY'] = "A092A34D-3FD8-4FF8-A32C-039785E3E4FD"
