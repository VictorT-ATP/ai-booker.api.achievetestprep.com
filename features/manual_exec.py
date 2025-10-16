from flask import Blueprint, render_template

manual_exec_bp = Blueprint('manual_exec', __name__)

@manual_exec_bp.route('')
def index():
    return render_template('manual_exec/index.html', title='Manual Contact')