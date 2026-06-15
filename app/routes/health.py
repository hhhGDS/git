#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
健康检查接口
"""

from flask import jsonify
from app.routes import health_bp


@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    健康检查端点
    
    Returns:
        JSON: {"code": 200, "status": "healthy"}
    """
    return jsonify({
        'code': 200,
        'status': 'healthy',
        'message': 'Service is running'
    })
