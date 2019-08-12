from flask import Flask, render_template

app = Flask(__name__)


class MyClass:
    def func(self):
        return 'This is a class function'


def my_function():
    return 'This is a function.'


@app.route('/')
def index():
    my_dict = {'type': 'dict'}
    my_list = ['list']
    my_class = MyClass()
    return render_template('02_jinja2_data/index.html', my_class=my_class, my_dict=my_dict,
                           my_function=my_function, my_list=my_list)


if __name__ == '__main__':
    app.run()
