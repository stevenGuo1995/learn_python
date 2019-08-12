from flask import Flask, redirect

app = Flask(__name__)


@app.route('/test')
def test():
    """
    默认访问地址为 localhost:5000/static/test.txt
    添加路由后可使用短地址访问（隐式访问）
    :return:
    """
    return app.send_static_file('test.txt')


@app.route('/redirect')
def abc():
    return redirect('static/test.txt')


if __name__ == '__main__':
    app.run()
