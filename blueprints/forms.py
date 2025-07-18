import wtforms
from wtforms.validators import Email, Length, EqualTo, DataRequired
from models import UserModle, EmailCaptcha
from exts import r, db

# Form: 主要验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message='邮箱格式错误')])  # Email还需要email-validator
    captcha = wtforms.StringField(validators=[Length(min=6, max=6, message='验证码格式错误')])
    username = wtforms.StringField(validators=[Length(min=3,max=20, message='用户名格式错误')])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message='密码格式错误')])
    password_confirm = wtforms.StringField(validators=[EqualTo('password', message='密码格式错误')])

    # 自定义验证:
    # 1.邮箱是否被注册
    def validate_email(self, field):
        email = field.data
        user = UserModle.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message='邮箱已经被注册')

    # 2.验证码是否正确
    def validate_captcha(self, field):
        captcha = field.data  # 用户输入的验证码
        email = self.email.data  # 拿到邮箱
        # Redis验证逻辑
        redis_captcha = r.get(f"email_captcha:{email}")
        if not redis_captcha or redis_captcha != captcha:
            raise wtforms.ValidationError(message='验证码错误')

        # 验证成功后删除redis中的验证码（可选）
        # r.delete(f"email_captcha:{email}")

        # 数据库验证
        # captcha_model = EmailCaptcha.query.filter_by(email=email, captcha=captcha).first()
        # if not captcha_model:
        #     raise wtforms.ValidationError(message='邮箱或验证码错误')

        # 定期清除，缺点频繁操作数据库影响性能
        # else:
        #     db.session.delete(captcha_model)
        #     db.session.commit()


