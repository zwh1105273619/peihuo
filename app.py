
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
app.debug = True

# 指定数据库路径，当前使用为sqlite数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True  # 将orm框架对数据库的操作转换为sql语言在控制台打印

db = SQLAlchemy(app)  # 创建sqlalchemy对象并绑定在app上


@app.route('/report/')
def report():
    path = r'F:\autotest\peihuo\result_file'
    file_list = []
    for file in os.listdir(path):
        if file.endswith('.xlsx'):
            file_list.append(file)

    return file_list


if __name__ == '__main__':
    app.run()
