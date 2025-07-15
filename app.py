from flask import Flask
import config
from exts import db
from models import UserModle

app = Flask(__name__)
# 从名为 config 的对象导入配置
app.config.from_object(config)

# 先创建后绑定
db.init_app(app)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
