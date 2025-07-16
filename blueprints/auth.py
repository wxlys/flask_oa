from flask import Blueprint, render_template
from exts import mail
from flask_mail import Message

bp = BLUEPRINT = Blueprint('auth', __name__, url_prefix='/auth')

# /auth/login
@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template("register.html")

# /auth/mail/test
@bp.route('/mail/test')
def mail_test():
    # 主题，收件人，内容
    message = Message('Test Message', recipients=['2419519923@qq.com'], body='Test Message')
    mail.send(message)
    return 'Mail successfully sent'