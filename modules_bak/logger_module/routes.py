from flask import Blueprint

logger_bp = Blueprint('logger', __name__, url_prefix='/logger')

@logger_bp.route('/status')
def logger_status():
    return {'status': 'Logger module bak is running'}