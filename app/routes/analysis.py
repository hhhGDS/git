#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数据分析接口
"""

from flask import request, jsonify, current_app
from app.routes import analysis_bp
from app.services.data_service import DataService


@analysis_bp.route('/analysis', methods=['POST'])
def analyze_data():
    """
    数据分析接口
    
    Request JSON:
        {
            "data": [...],
            "analysis_type": "statistical|trend|correlation",
            "model": "deepseek|qwen"
        }
    
    Returns:
        JSON: {"code": 200, "data": {...}}
    """
    try:
        data = request.get_json()
        
        if not data or 'data' not in data:
            return jsonify({
                'code': 400,
                'message': '请提供要分析的数据'
            }), 400
        
        analysis_data = data.get('data')
        analysis_type = data.get('analysis_type', 'statistical')
        model = data.get('model', 'deepseek')
        
        service = DataService(current_app.config)
        result = service.analyze(analysis_data, analysis_type, model)
        
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': result
        })
        
    except Exception as e:
        current_app.logger.error(f'Analysis error: {str(e)}')
        return jsonify({
            'code': 500,
            'message': '分析出错',
            'error': str(e)
        }), 500
