#!/usr/bin/env python
# -*- coding: utf-8 -*-
"日志工具"
import os
import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name='app', log_level='INFO', log_file=None):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    level = getattr(logging, log_level.upper(), logging.INFO)
    logger.setLevel(level)
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt, datefmt='%Y-%m-%d %H:%M:%S')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        fh = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger


def get_logger(name='app'):
    return logging.getLogger(name)
