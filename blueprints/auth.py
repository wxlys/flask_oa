from flask import Blueprint, render_template,jsonify
from exts import mail, r, db
from flask_mail import Message
from flask import request
import string, random

from models import EmailCaptcha

bp = BLUEPRINT = Blueprint('auth', __name__, url_prefix='/auth')

# /auth/login
@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template("register.html")

# bp.route:而果没有指定methods参数，默认就是GET请求
@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    captcha_code = f"{random.randint(0, 999999):06d}"
    print(captcha_code)
    message = Message('注册验证码', recipients=[email], body=f'您的注册验证码是：{captcha_code}')
    mail.send(message)
    # 存储到redis，设置5分钟过期
    r.setex(f"email_captcha:{email}", 300, captcha_code)
    # 存储到数据库中
    # email_captcha = EmailCaptcha(email=email, captcha_code=captcha_code)
    # db.session.add(email_captcha)
    # db.session.commit()
    return jsonify({'code': 200, 'message': '', 'data': None})

# /auth/mail/test
@bp.route('/mail/test')
def mail_test():
    # 主题，收件人，内容
    message = Message('Test Message', recipients=['2419519923@qq.com'], body='Test Message')
    mail.send(message)
    return 'Mail successfully sent'