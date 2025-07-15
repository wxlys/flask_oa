from flask import Blueprint

# 名称--固定写法--前缀
bp = BLUEPRINT = Blueprint('qa', __name__, url_prefix='/')

# http://127.0.0.1:5000/
@bp.route('/')
def index():
    pass

