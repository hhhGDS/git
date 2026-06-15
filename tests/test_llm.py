#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""LLM服务测试"""
import pytest
from app.models.llm import DeepSeekModel, QwenModel
from app.services.llm_service import LLMService


class TestLLMModels:
    def setup_method(self):
        self.config = {'DEEPSEEK_API_KEY': 'test', 'QWEN_API_KEY': 'test'}

    def test_deepseek_model(self):
        model = DeepSeekModel(self.config)
        info = model.get_model_info()
        assert info['model'] == 'deepseek'
        result = model.chat('你好')
        assert 'model_used' in result

    def test_qwen_model(self):
        model = QwenModel(self.config)
        info = model.get_model_info()
        assert info['model'] == 'qwen'
        result = model.chat('你好')
        assert 'model_used' in result

    def test_llm_service(self):
        service = LLMService(self.config)
        result = service.chat('你好', 'deepseek')
        assert result['model_used'] == 'deepseek'

    def test_unsupported_model(self):
        service = LLMService(self.config)
        with pytest.raises(ValueError):
            service.chat('你好', 'unsupported')
