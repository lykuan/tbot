# Telegram Amazon Affiliate Bot

这是一个Telegram机器人，用于处理Amazon产品链接并创建带有Affiliate ID的推广消息。

## 功能

- 接收Amazon产品链接
- 获取产品详细信息
- 生成格式化的产品介绍
- 支持图片和文本消息
- 自动添加Affiliate ID
- HTML格式化输出

## 安装

1. 克隆仓库:
```bash
git clone <your-repository-url>
cd telegram-amazon-bot
```

2. 安装依赖:
```bash
pip install -r requirements.txt
```

3. 配置constants.py:
```python
# Telegram配置
TELEGRAM_TOKEN = "你的Telegram机器人Token"
CHANNEL_ID = "目标频道ID"

# Amazon配置
AMAZON_ACCESS_KEY = "你的Amazon访问密钥"
AMAZON_SECRET_KEY = "你的Amazon密钥"
PARTNER_TAG = "你的Associate ID"
AMAZON_REGION = "us-east-1"
```

## 运行

```bash
python bot.py
```

## 部署选项

1. Hugging Face Spaces (免费，无需信用卡)
2. Oracle Cloud (免费，需要信用卡验证)
3. Railway.app (有免费额度)
4. Render.com (有免费额度)

详细部署说明请参考代码注释。

## License

MIT

## 鸣谢

- 基于原始项目修改
- 添加了代理支持
- 优化了错误处理
- 增加了HTML格式化
