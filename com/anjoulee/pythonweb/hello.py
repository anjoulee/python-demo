# coding = utf-8

from flask import Flask  ###导出Flask类

app = Flask(__name__)  ###生成一个web APP对象


@app.route('/')  ###注册一个URL，表示当请求'/',这个网址时，执行hello_world函数
def hello_world():
    return 'hello,every one'


if __name__ == '__main__':
    app.run();
    ###启动这个APP应用
    ###相关参数：app.run(host=None,port=None,debug=None,**options)
    ###host默认127.0.0.1
    ###port 默认是：5000
