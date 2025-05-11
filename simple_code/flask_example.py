from flask import Flask
import time
import functools

app = Flask(__name__)


def delay_decorator(function):
    @functools.wraps(function)
    def wrapper_func():
        time.sleep(2)
        return  function()
    return wrapper_func

@app.route('/')
@delay_decorator
def hello_world():
    print('123456')
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)