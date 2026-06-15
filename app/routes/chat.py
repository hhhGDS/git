#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
聊天接口
"""

from flask import request, jsonify, current_app
from app.routes import chat_bp
from app.services.llm_service import LLMService
from app.utils.validators import validate_chat_request


@chat_bp.route('/chat', methods=['POST'])
def chat():
    """
    智能聊天接口
    
    Request JSON:
        {
            "message": "用户消息",
            "model": "deepseek|qwen",
            "context": {}
        }
    
    Returns:
        JSON: {"code": 200, "data": {...}}
    """
    try:
        data = request.get_json()
        
        # 验证请求
        errors = validate_chat_request(data)
        if errors:
            return jsonify({
                'code': 400,
                'message': '请求参数错误',
                'errors': errors
            }), 400
        
        message = data.get('message')
        model = data.get('model', 'deepseek')
        context = data.get('context', {})
        
        # 调用LLM服务
        service = LLMService(current_app.config)
        response = service.chat(message, model, context)
        
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': response
        })
        
    except Exception as e:
        current_app.logger.error(f'Chat error: {str(e)}')
        return jsonify({
            'code': 500,
            'message': '处理请求出错',
            'error': str(e)
        }), 500
