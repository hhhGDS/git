#!/usr/bin/env python
# -*- coding: utf-8 -*-
\"\"\"
LLM 模型封装

定义不同大语言模型的统一接口封装。
\"\"\"

from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


class LLMModel(ABC):
    \"\"\"LLM 模型基类，定义统一接口\"\"\"

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.api_key = ''
        self.api_url = ''
        self.model_name = ''

    @abstractmethod
    def chat(self, message: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        ...

    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        ...


class DeepSeekModel(LLMModel):
    \"\"\"DeepSeek 模型封装\"\"\"

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config.get('DEEPSEEK_API_KEY', '')
        self.api_url = config.get('DEEPSEEK_API_URL', 'https://api.deepseek.com/v1')
        self.model_name = 'deepseek-chat'

    def chat(self, message: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        return {'response': f'DeepSeek: {message}', 'model_used': 'deepseek', 'model_name': self.model_name, 'tokens_used': 100}

    def get_model_info(self) -> Dict[str, Any]:
        return {'model': 'deepseek', 'model_name': self.model_name, 'provider': 'DeepSeek'}


class QwenModel(LLMModel):
    \"\"\"通义千问模型封装\"\"\"

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config.get('QWEN_API_KEY', '')
        self.api_url = config.get('QWEN_API_URL', 'https://dashscope.aliyuncs.com/api/v1')
        self.model_name = 'qwen-plus'

    def chat(self, message: str, context: Optional[Dict] = None) -> Dict[str, Any]:
        return {'response': f'\u901a\u4e49\u5343\u95ee: {message}', 'model_used': 'qwen', 'model_name': self.model_name, 'tokens_used': 100}

    def get_model_info(self) -> Dict[str, Any]:
        return {'model': 'qwen', 'model_name': self.model_name, 'provider': 'Alibaba Cloud'}
