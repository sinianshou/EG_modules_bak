import os
import logging
from logging.handlers import RotatingFileHandler
from .routes import logger_bp

def init_logger_module(app):
    """初始化日志模块"""
    # 注册蓝图
    app.register_blueprint(logger_bp)
    
    # 设置日志级别
    log_level = logging.DEBUG if os.getenv('FLASK_ENV', 'production') == 'development' else logging.WARNING
    
    # 确保日志目录存在
    log_dir = os.path.join(app.root_path, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # 配置日志文件
    log_file = os.path.join(log_dir, 'app.log')
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d: \n %(message)s"
    )
    
    # 设置应用日志级别
    app.logger.setLevel(log_level)
    
    # 配置文件处理器
    handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    handler.setLevel(log_level)
    handler.setFormatter(formatter)
    
    # 配置控制台处理器
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(log_level)
    streamHandler.setFormatter(formatter)
    
    # 清理现有处理器并添加新处理器
    app.logger.handlers = [handler, streamHandler]
    
    app.logger.info(f"Logger module initialized with level: {logging.getLevelName(log_level)}")