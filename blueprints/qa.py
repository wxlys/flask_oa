from flask import Blueprint, render_template

# 名称--固定写法--前缀
bp = BLUEPRINT = Blueprint('qa', __name__, url_prefix='/')

# http://127.0.0.1:5000/
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/public_question')
def public_question():
    return render_template('public_question.html')

@bp.route('/search')
def search():
    pass

