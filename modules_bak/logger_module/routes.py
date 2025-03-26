from flask import Blueprint, current_app
import logging

logger_bp = Blueprint('logger', __name__, url_prefix='/logger')

@logger_bp.route('/status')
def logger_status():
    current_app.logger.debug('Debug log test')
    current_app.logger.info('Info log test')
    current_app.logger.warning('Warning log test')
    return {
        'status': 'Logger module is running', 
        'level': logging.getLevelName(current_app.logger.getEffectiveLevel())
    }