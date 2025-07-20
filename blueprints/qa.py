from flask import Blueprint, render_template, request, g, url_for, redirect

from exts import db
from .forms import QuestionForm
from models import Question

# 名称--固定写法--前缀
bp = BLUEPRINT = Blueprint('qa', __name__, url_prefix='/')

# http://127.0.0.1:5000/
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/public_question', methods=['GET', 'POST'])
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate:
            title = form.title.data
            content = form.content.data
            question = Question(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            print(form.errors)
            return redirect(url_for('qa.public_question'))


@bp.route('/search')
def search():
    pass

