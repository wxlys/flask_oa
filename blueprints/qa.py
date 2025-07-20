from flask import Blueprint, render_template, request, g, url_for, redirect

from exts import db
from .forms import QuestionForm, AnswerForm
from models import Question, AnswerModel
from decorators import login_decorator

# 名称--固定写法--前缀
bp = BLUEPRINT = Blueprint('qa', __name__, url_prefix='/')

# http://127.0.0.1:5000/
@bp.route('/')
def index():
    question = Question.query.order_by(Question.create_time.desc()).all()
    return render_template('index.html',questions=question)

@bp.route('/qa/public_question', methods=['GET', 'POST'])
@login_decorator
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate:
            title = form.title.data
            content = form.content.data
            # author=g.user 需要对未登录进行处理以免崩溃
            question = Question(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            print(form.errors)
            return redirect(url_for('qa.public_question'))

# 搜索视图函数
@bp.route('/qa/search')
def search():
    # 获取用户要查询的内容
    # /search?q=flask
    # /search/<q>
    # post, request.form
    q = request.args.get('q') # 用户所提交的q的对应值

    # 从数据库表中查询  title.contains(q) 标题包含q
    question = Question.query.filter(Question.title.contains(q)).all()
    return render_template('index.html', questions=question)

@bp.route('/qa/qa_detail/<qa_id>')
def qa_detail(qa_id):
    question = Question.query.get(qa_id)
    return render_template('detail.html', question=question)

@bp.route('/answer/public', methods=['POST'])
@login_decorator
def public_answer():
    form = AnswerForm(request.form)
    if form.validate:
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content, question_id=question_id, author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        # qa.qa_detail
        # 系统提示缺少 qa_id 参数     detail在判断pq_id=()
        return redirect(url_for('qa.qa_detail', qa_id=question_id))
    else:
        print(form.errors)
        return redirect(url_for('qa.qa_detail', qa_id=request.form.get("question_id")))


