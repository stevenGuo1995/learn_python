from flask import Flask

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run()
