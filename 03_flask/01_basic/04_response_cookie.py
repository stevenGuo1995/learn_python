from flask import Flask, request, make_response
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/')
def index():
    response = make_response('<h1>This document is response test.</h1>')
    return response


@app.route('/write_cookie/<cv>')
def write_cookie(cv):
    response = make_response('<h1>Cookie write success!</h1>')
    out_date = datetime.today() + timedelta(seconds=20)
    # 指定cookie过期时间
    response.set_cookie('cv', cv, expires=out_date)
    return response


@app.route('/read_cookie')
def read_cookie():
    value = request.cookies.get('cv')
    print(value)
    if value is None:
        value = '<h1>Cookie is not exist!</h1>'
    return value


if __name__ == '__main__':
    app.run()
