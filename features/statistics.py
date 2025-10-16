from flask import Blueprint, render_template

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('')
def index():
    return render_template('statistics/index.html', title='Statistics')