#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask应用工厂
"""

from flask import Flask
from flask_cors import CORS
from app.config import config_by_name


def create_app(config_name='development'):
    """
    应用工厂函数
    
    Args:
        config_name: 配置名称 (development, production, testing)
    
    Returns:
        Flask应用实例
    """
    app = Flask(__name__)
    
    # 加载配置
    app.config.from_object(config_by_name[config_name])
    
    # 初始化CORS
    CORS(app, 
         origins=app.config.get('CORS_ORIGINS', '*'),
         allow_headers=app.config.get('CORS_ALLOW_HEADERS', ['Content-Type', 'Authorization']))
    
    # 注册蓝图
    from app.routes import chat_bp, health_bp, analysis_bp
    
    app.register_blueprint(chat_bp, url_prefix='/api')
    app.register_blueprint(health_bp, url_prefix='/api')
    app.register_blueprint(analysis_bp, url_prefix='/api')
    
    # 错误处理器
    @app.errorhandler(400)
    def bad_request(error):
        return {'code': 400, 'message': '请求参数错误'}, 400
    
    @app.errorhandler(404)
    def not_found(error):
        return {'code': 404, 'message': '接口不存在'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'code': 500, 'message': '服务器内部错误'}, 500
    
    return app
