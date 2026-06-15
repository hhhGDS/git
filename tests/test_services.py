#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""服务层测试"""
import pytest
from app.services.llm_service import LLMService
from app.services.data_service import DataService
from app.services.nlp_service import NLPService


class TestServices:
    def setup_method(self):
        self.config = {'DEEPSEEK_API_KEY': 'test', 'QWEN_API_KEY': 'test'}

    def test_data_statistical(self):
        service = DataService(self.config)
        data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
        result = service.analyze(data, 'statistical')
        assert result['analysis_type'] == 'statistical'
        assert result['total_rows'] == 2

    def test_nlp_sentiment(self):
        service = NLPService(self.config)
        result = service.analyze_sentiment('这个产品好极了')
        assert result['sentiment'] == 'positive'

    def test_nlp_keywords(self):
        service = NLPService(self.config)
        keywords = service.extract_keywords('今天天气真好，适合去海边散步')
        assert len(keywords) > 0
