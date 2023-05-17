from flask import (Blueprint, render_template, request, redirect)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    return 'This is the facts index'
    