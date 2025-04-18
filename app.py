from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'
PASSWORD = '123456'  # 修改为你自己的密码

# 初始化数据文件
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"content": "今天还没有分享内容~"}, f)

@app.route('/')
def index():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return render_template('index.html', content=data['content'])

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        pwd = request.form.get('password')
        content = request.form.get('content')
        if pwd == PASSWORD:
            with open(DATA_FILE, 'w') as f:
                json.dump({"content": content}, f)
            return redirect(url_for('index'))
        else:
            return render_template('admin.html', error="密码错误！")
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
