from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('01_render_html/index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('01_render_html/user.html', name=name)


if __name__ == '__main__':
    # 指定ip和端口号
    app.run(host='0.0.0.0', port='1234')
