#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WSGI入口点 - 用于Gunicorn等WSGI服务器
"""

import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()

app = create_app(os.getenv('FLASK_ENV', 'production'))

if __name__ == '__main__':
    app.run()
