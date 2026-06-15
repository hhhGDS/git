#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
路由模块
"""

from flask import Blueprint

# 创建蓝图
chat_bp = Blueprint('chat', __name__)
health_bp = Blueprint('health', __name__)
analysis_bp = Blueprint('analysis', __name__)

# 导入路由
from app.routes.chat import *
from app.routes.health import *
from app.routes.analysis import *
