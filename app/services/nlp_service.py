#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NLP服务 - 自然语言处理"""
import re
from typing import Dict, Any, List


class NLPService:
    """自然语言处理服务"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """简单情感分析"""
        positive_words = ['好', '棒', '喜欢', '优秀', '赞', '开心', '满意', 'great', 'good', 'love', 'excellent']
        negative_words = ['差', '坏', '讨厌', '垃圾', '烂', '难过', '不满', 'bad', 'terrible', 'hate', 'awful']
        text_lower = text.lower()
        pos_count = sum(1 for w in positive_words if w in text_lower)
        neg_count = sum(1 for w in negative_words if w in text_lower)
        total = pos_count + neg_count
        if total == 0:
            return {'sentiment': 'neutral', 'score': 0.5, 'positive': 0.5, 'negative': 0.5}
        score = pos_count / total
        return {'sentiment': 'positive' if score > 0.6 else 'negative' if score < 0.4 else 'neutral',
                'score': round(score, 2), 'positive': pos_count, 'negative': neg_count}

    def extract_keywords(self, text: str, max_keywords: int = 5) -> List[str]:
        """简单关键词提取"""
        stop_words = {'的', '了', '在', '是', '我', '有', '和', '就', '不', '人', '都', '一', '一个', '上', '也', '很',
                      '到', '说', '要', '去', '你', '会', '着', '没有', '看', '好', '自己', '这', '他', '她', '它',
                      '们', '那', '对', '为', '能', '得', '与', '及', '但', '而', '或', '被', '把', '让', '从', '向'}
        words = re.findall(r'[\w]+', text)
        word_freq = {}
        for w in words:
            if w.lower() not in stop_words and len(w) > 1:
                word_freq[w] = word_freq.get(w, 0) + 1
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [w for w, _ in sorted_words[:max_keywords]]

    def summarize(self, text: str, max_length: int = 100) -> str:
        """简单文本摘要"""
        if len(text) <= max_length:
            return text
        sentences = re.split(r'[。！？.!?\n]', text)
        result = ''
        for s in sentences:
            if len(result) + len(s) + 1 <= max_length:
                result += s + '。' if s else ''
            else:
                break
        return result.strip() + '...' if len(text) > len(result) else result.strip()
