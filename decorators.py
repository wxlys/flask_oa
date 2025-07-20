from functools import wraps
from flask import g, redirect, url_for

def login_decorator(func):
    # 在执行wrapper时保留func的信息
    @wraps(func)
    def wrapper(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('auth.login'))
    return wrapper