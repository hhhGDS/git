#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""聊天模型"""
from typing import Dict, Any, List, Optional
from datetime import datetime


class ChatMessage:
    """单条聊天消息"""

    def __init__(self, role: str, content: str, timestamp: Optional[datetime] = None):
        self.role = role
        self.content = content
        self.timestamp = timestamp or datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        return {'role': self.role, 'content': self.content, 'timestamp': self.timestamp.isoformat()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ChatMessage':
        return cls(role=data['role'], content=data['content'])


class ChatSession:
    """聊天会话"""

    def __init__(self, session_id: str, model: str = 'deepseek'):
        self.session_id = session_id
        self.model = model
        self.messages: List[ChatMessage] = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_message(self, role: str, content: str) -> ChatMessage:
        msg = ChatMessage(role=role, content=content)
        self.messages.append(msg)
        self.updated_at = datetime.now()
        return msg

    def get_context(self) -> List[Dict[str, str]]:
        return [{'role': m.role, 'content': m.content} for m in self.messages[-10:]]

    def to_dict(self) -> Dict[str, Any]:
        return {'session_id': self.session_id, 'model': self.model,
                'messages': [m.to_dict() for m in self.messages],
                'created_at': self.created_at.isoformat(), 'updated_at': self.updated_at.isoformat()}
