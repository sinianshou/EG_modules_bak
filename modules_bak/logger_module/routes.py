from flask import Blueprint, current_app
import logging

logger_bp = Blueprint('logger', __name__, url_prefix='/logger')

@logger_bp.route('/status')
def logger_status():
    """获取日志模块状态
    ---
    tags:
      - Logger
    responses:
      200:
        description: 日志模块状态信息
        schema:
          properties:
            status:
              type: string
              description: 模块运行状态
            level:
              type: string
              description: 当前日志级别
    """
    current_app.logger.debug('Debug log test')
    current_app.logger.info('Info log test')
    current_app.logger.warning('Warning log test')
    return {
        'status': 'Logger module is running', 
        'level': logging.getLevelName(current_app.logger.getEffectiveLevel())
    }