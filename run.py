#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
本地开发运行脚本
"""

import os
from dotenv import load_dotenv
from app import create_app

# 加载环境变量
load_dotenv()

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV', 'development'))
    app.run(
        host=os.getenv('HOST', '0.0.0.0'),
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('FLASK_DEBUG', True)
    )
