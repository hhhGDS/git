#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数据验证工具
"""

from typing import Dict, Any, List


def validate_chat_request(data: Dict[str, Any]) -> List[str]:
    """
    验证聊天请求
    
    Args:
        data: 请求数据
    
    Returns:
        List: 错误信息列表
    """
    errors = []
    
    if not data:
        errors.append('请求体为空')
        return errors
    
    if 'message' not in data:
        errors.append('缺少必需字段: message')
    elif not isinstance(data['message'], str):
        errors.append('message 必须是字符串')
    elif len(data['message'].strip()) == 0:
        errors.append('message 不能为空')
    
    if 'model' in data:
        if data['model'] not in ['deepseek', 'qwen']:
            errors.append('model 只能是 deepseek 或 qwen')
    
    return errors
