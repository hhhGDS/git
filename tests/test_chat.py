#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""聊天接口测试"""
import json
import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app('testing')
    return app


@pytest.fixture
def client(app):
    return app.test_client()


class TestChat:
    def test_chat_success(self, client):
        resp = client.post('/api/chat', json={'message': '你好', 'model': 'deepseek'})
        data = resp.get_json()
        assert resp.status_code == 200
        assert data['code'] == 200

    def test_chat_missing_message(self, client):
        resp = client.post('/api/chat', json={})
        assert resp.status_code == 400

    def test_chat_empty_message(self, client):
        resp = client.post('/api/chat', json={'message': ''})
        assert resp.status_code == 400

    def test_chat_invalid_model(self, client):
        resp = client.post('/api/chat', json={'message': 'hi', 'model': 'invalid'})
        assert resp.status_code == 400
