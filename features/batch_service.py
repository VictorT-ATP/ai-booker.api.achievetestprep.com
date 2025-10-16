from flask import Blueprint, render_template

batch_service_bp = Blueprint('batch_service', __name__)

@batch_service_bp.route('')
def index():
    return render_template('batch_service/index.html', title='Batch Service')