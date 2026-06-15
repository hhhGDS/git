#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
配置管理
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    基础配置
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Flask配置
    JSON_SORT_KEYS = False
    JSON_ENSURE_ASCII = False
    
    # CORS配置
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')
    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization']
    
    # LLM配置
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY', '')
    DEEPSEEK_API_URL = os.getenv('DEEPSEEK_API_URL', 'https://api.deepseek.com/v1')
    
    QWEN_API_KEY = os.getenv('QWEN_API_KEY', '')
    QWEN_API_URL = os.getenv('QWEN_API_URL', 'https://dashscope.aliyuncs.com/api/v1')
    
    # 日志配置
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/app.log')
    
    # 速率限制
    RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'True') == 'True'
    RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_PER_MINUTE', 60))


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """
    生产环境配置
    """
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """
    测试环境配置
    """
    DEBUG = True
    TESTING = True
    DEEPSEEK_API_KEY = 'test-key'
    QWEN_API_KEY = 'test-key'


config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
