# 01 Flask基础知识

## 1.1 flask框架

```python
from flask import Flask

app = Flask(__name__)

# 定义路由（就是访问的网址）
@app.route('/')
def hello_world():
    # 返回的网页内容
    return 'Hello World!'

# 运行flask
if __name__ == '__main__':
    app.run()
```

## 2.2 静态路由和动态路由

```python
@app.route('/static_route')
def static_route():
    """
    静态路由
    :return: 
    """
    return 'This is a static route!'
@app.route('/dynamic_route/<name>')
def dynamic_route(name):
    """
    动态路由，动态加载参数
    :param name: 
    :return: 
    """
    return 'Hi, {}, this is a dynamic route!'.format(name)


@app.route('/dynamic_route/steven')
def dynamic_vs_static():
    """
    当动态路由和静态路由重复时，优先加载静态路由
    :return:
    """
    return 'Steven, this is a static route!'
@app.route('/dynamic/<a1>-<a2>-<a3>')
def multi_param(a1, a2, a3):
    """
    同时输入多个参数，也可写成<a1>/<a2> 的形式
    :param a1: 
    :param a2: 
    :param a3: 
    :return: 
    """
    return '{}#{}#{}'.format(a1, a2, a3)

```

## 1.3 获取请求

```python	
@app.route('/')
def index():
    """
    获取head请求头
        Keys: {
                Host:
                Connection:
                Cache-Control:
                Requests:
                User-Agent:
                Accept:
                Cookie:
                }
    :return:
    """
    user_agent = request.headers.get("User-Agent")
    return '<h1>Your agent is <p>{}</p></h1>'.format(user_agent)
@app.route('/get')
def get():
    """
    get传值：
    如，访问
        http://127.0.0.1:5000/get?arg=1234
    会返回，arg的值
    :return:
    """
    value = request.args.get('arg')
    return '<h1>Your get param is <p>{}</p></h1>'.format(value)
```

## 1.4 cookie, seesion, response

## 1.5 静态文件与重定向

