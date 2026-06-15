#!/usr/bin/env python
# -*- coding: utf-8 -*-
"装饰器工具"
import functools
import time
import logging
from flask import request, jsonify

logger = logging.getLogger(__name__)


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        logger.info(f'{func.__name__} took {elapsed:.3f}s')
        return result
    return wrapper


def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Request: {request.method} {request.path}')
        return func(*args, **kwargs)
    return wrapper


def require_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not request.is_json:
            return {'code': 400, 'message': '请求必须是JSON格式'}, 400
        return func(*args, **kwargs)
    return wrapper


def handle_errors(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return {'code': 400, 'message': str(e)}, 400
        except Exception:
            logger.exception('Unexpected error')
            return {'code': 500, 'message': '服务器内部错误'}, 500
    return wrapper
