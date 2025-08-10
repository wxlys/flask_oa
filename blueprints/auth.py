from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from huggingface_hub import User
from exts import mail, r, db
from flask_mail import Message
from flask import request
import string, random
from .forms import RegisterForm, LoginForm
from models import EmailCaptcha, UserModle
from werkzeug.security import generate_password_hash, check_password_hash  # 哈希加密

bp = BLUEPRINT = Blueprint('auth', __name__, url_prefix='/auth')

# /auth/login
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModle.query.filter_by(email=email).first()
            if not user:
                # todo: 文本框提示或弹出消息
                print("User not found")
                return redirect(url_for('auth.login'))
            if check_password_hash(user.password, password):
                # cookie
                # 1.其中不太适合存放大量的数据
                # 2.一般用来存放授权等信息
                # flask中的session是加密后存储在cookie中的
                session['user_id'] = user.id
                return redirect('/')
            else:
                # todo: 文本框提示或弹出消息
                print("password incorrect")
                return redirect(url_for('auth.login'))
        else:
            print(form.errors)
            return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        form = RegisterForm(request.form)  # request.form 用户提交的数据
        if form.validate():  # 所有信息需要通过验证器验证才能进行存储
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # 创建用户并保存到数据库
            try:
                user = UserModle(email=email, username=username, password=generate_password_hash(password)) # 密码哈希加密存储
                db.session.add(user)
                db.session.commit()
                # 注册成功，跳转登录页面   from flask import redirect 重新指向
                return redirect(url_for('auth.login'))  # 将视图函数转换为url填充
            except Exception as e:
                db.session.rollback()   # 出错时回滚
                print(f"注册出错：{e}")
                return redirect(url_for('auth.register'))
        else:
            # 表单验证失败
            print(form.errors)
            return redirect(url_for('auth.register'))

#
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

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))