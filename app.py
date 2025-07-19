from flask import Flask, session, g
import config
from exts import db
from models import UserModle
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
# 从名为 config 的对象导入配置
app.config.from_object(config)

# 先创建后绑定
db.init_app(app)
mail = Mail(app)

migrate = Migrate(app, db)

# 注册蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

# before_request/before_first_request/after_request  钩子函数
# hook

# 抢在在执行视图函数前，获取用户id
@app.before_request
def before_request():
    # 取session中的userid
    user_id = session.get('user_id')
    if user_id:
        user = UserModle.query.get(user_id)
        # g 全局对象
        # 绑定
        setattr(g, 'user', user)
    # 属性为None  如果没有的话：当user_id不匹配时g.user不存在产生报错
    else:
        setattr(g, 'user', None)

# 上下文处理器：在这里返回什么变量，在其他模板中就会有这个变量
@app.context_processor
def my_context_processor():
    return {'user': g.user}

if __name__ == '__main__':
    app.run()
