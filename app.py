import os
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# 获取端口环境变量（如果没有，默认为 5000）
port = int(os.environ.get('PORT', 5000))

@app.route('/')
def home():
    # 示例：在主页上显示简单的内容
    return 'Hello, Daily Node Share!'

if __name__ == '__main__':
    # 绑定到 0.0.0.0，使用从环境变量读取的端口
    app.run(host='0.0.0.0', port=port, debug=True)
