from flask import Flask, request, session
from datetime import timedelta

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return '{}，已登录'.format(session['username'])
    return '未登录'


@app.route('/login')
def login():
    session['username'] = request.args.get('username')
    return '登录成功'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return '注销成功'


app.secret_key = 'asdasdasdasd'
app.permanent_session_lifetime = timedelta(seconds=20)


if __name__ == '__main__':
    app.run()
