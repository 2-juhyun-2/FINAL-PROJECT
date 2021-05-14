from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from policy import db
from policy.forms import UserLoginForm
from policy.forms import UserCreateForm
from policy.models import User
import datetime

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "User does not exist!"
        elif not check_password_hash(user.password, form.password.data):
            error = "Invalid password!"
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.index')) # 수정하기
        flash(error)
    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index')) # 수정



@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data,
            password=generate_password_hash(form.password1.data),
            email=form.email.data,
            level=form.level.data)
           

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))

        else:
            flash('이미 존재하는 사용자입니다.')
    
    return render_template('auth/signup.html', form=form)
    