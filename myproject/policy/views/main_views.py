from flask import Blueprint
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello'


@bp.route('/')
def index():
    return 'index'