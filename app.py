from flask import Flask
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

if __name__ == '__main__':
    app.run()
