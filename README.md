# Python多功能智能助手

基于Flask搭建的多功能智能助手后端系统，结合LangChain大模型调度能力与自然语言处理、数据分析相关技术，无缝接入 DeepSeek 与通义千问两款主流大模型实现智能对话交互。

## 🎯 项目特点

- ✅ **多模型支持** - 集成DeepSeek、通义千问等主流大模型
- ✅ **LangChain调度** - 强大的大模型编排和链式调用能力
- ✅ **自然语言处理** - 文本分析、理解与生成
- ✅ **数据分析** - 结构化数据处理与可视化
- ✅ **跨域配置** - 完整的CORS配置支持
- ✅ **环境管理** - 灵活的配置管理系统
- ✅ **生产级部署** - Docker、Gunicorn等生产配置
- ✅ **稳定性保障** - 错误处理、日志记录、健康检查

## 📋 项目结构

```
Python-AI-Assistant/
├── app/
│   ├── __init__.py              # Flask应用工厂
│   ├── config.py                # 配置管理
│   ├── models/
│   │   ├── __init__.py
│   │   ├── llm.py               # LLM模型封装
│   │   └── chat.py              # 聊天模型
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── chat.py              # 聊天接口
│   │   ├── analysis.py          # 数据分析接口
│   │   └── health.py            # 健康检查
│   ├── services/
│   │   ├── __init__.py
│   │   ├── llm_service.py       # LLM服务
│   │   ├── nlp_service.py       # NLP服务
│   │   └── data_service.py      # 数据分析服务
│   └── utils/
│       ├── __init__.py
│       ├── logger.py            # 日志工具
│       ├── decorators.py        # 装饰器
│       └── validators.py        # 数据验证
├── tests/
│   ├── __init__.py
│   ├── test_chat.py
│   ├── test_llm.py
│   └── test_services.py
├── config/
│   ├── development.py           # 开发环境配置
│   ├── production.py            # 生产环境配置
│   └── testing.py               # 测试环境配置
├── .env.example                 # 环境变量示例
├── requirements.txt             # 依赖包列表
├── wsgi.py                      # WSGI入口
├── run.py                       # 本地开发运行
├── Dockerfile                   # Docker配置
├── docker-compose.yml           # Docker Compose
└── README.md                    # 项目说明
```

## 🚀 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/hhhGDS/git.git
cd git

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量

```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env 文件，添加API密钥
# DEEPSEEK_API_KEY=your_key
# QWEN_API_KEY=your_key
# FLASK_ENV=development
```

### 3. 本地运行

```bash
python run.py
```

访问 `http://localhost:5000`

### 4. Docker部署

```bash
# 构建镜像
docker build -t python-ai-assistant .

# 运行容器
docker run -p 5000:5000 --env-file .env python-ai-assistant

# 或使用 Docker Compose
docker-compose up -d
```

## 📚 API文档

### 1. 智能对话

**POST** `/api/chat`

```json
{
  "message": "你好，帮我分析一下这个数据",
  "model": "deepseek",
  "context": {}
}
```

**响应**

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "response": "AI回复内容",
    "model_used": "deepseek",
    "tokens_used": 150
  }
}
```

### 2. 数据分析

**POST** `/api/analysis`

```json
{
  "data": [...],
  "analysis_type": "statistical",
  "model": "qwen"
}
```

### 3. 健康检查

**GET** `/api/health`

## 🔧 核心配置

### 支持的LLM模型

- **DeepSeek** - 高效的大语言模型
- **通义千问** - 阿里巴巴的大模型
- 可扩展支持其他模型

### 环境变量

```
FLASK_ENV=development
FLASK_DEBUG=True
DEEPSEEK_API_KEY=
QWEN_API_KEY=
DATABASE_URL=
LOG_LEVEL=INFO
CORS_ORIGINS=*
```

## 🧪 测试

```bash
# 运行单元测试
pytest tests/ -v

# 生成覆盖率报告
pytest tests/ --cov=app --cov-report=html
```

## 📦 依赖库

- **Flask** - Web框架
- **LangChain** - LLM编排框架
- **OpenAI API** - DeepSeek/Qwen接口
- **Pandas** - 数据分析
- **Requests** - HTTP客户端
- **Python-dotenv** - 环境变量管理
- **Gunicorn** - WSGI服务器

## 🔐 安全建议

- 不要在代码中硬编码API密钥
- 使用环境变量管理敏感信息
- 启用CORS白名单限制
- 实施请求频率限制
- 定期更新依赖包

## 📝 更新日志

### v1.0.0 (2026-06-15)
- ✅ 项目初始化
- ✅ 基础架构搭建
- ✅ API框架设计

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 👨‍💻 作者

**hhhGDS**

---

💡 **提示**：详细的开发文档请查看 `docs/` 目录
