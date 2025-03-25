# 使用绝对导入路径
from .routes import logger_bp

def init_logger_module(app):
    # 注册路由
    app.register_blueprint(logger_bp)
    print("✅ [Logger] 日志模块已加载")