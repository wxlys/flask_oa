from flask import Blueprint, render_template

bp = BLUEPRINT = Blueprint('auth', __name__, url_prefix='/auth')

# /auth/login
@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template("register.html")