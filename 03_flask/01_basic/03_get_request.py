from flask import Flask, request

app = Flask(__name__)


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


@app.route('/header')
def header():
    user_agent = request.headers
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


if __name__ == '__main__':
    app.run()
