from flask import Blueprint, render_template

leads_bp = Blueprint('leads', __name__)

@leads_bp.route('')
def index():
    return render_template('leads/index.html', title='Leads to Contact')