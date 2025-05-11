from flask import Flask
import time

app = Flask(__name__)


def delay_decorator(function):
    def wrapper_func():
        time.sleep(2)
        return  function()
    return wrapper_func

def make_bold(function):
    def wrapper():
        print('2')
        return "<b style='color: red'>" + function() + "</b>"
    return wrapper

def make_underlined(function):
    def wrapper():
        print('3')
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bold')
@make_bold
@make_underlined
def bold():
    print('1')
    return 'AAAAA'

@app.route('/')
@delay_decorator
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def bye():
    return 'Bye!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/html')
def html():
    return '''
    <html>
        <head>
            <title>Take Off</title>
        </head>
        <body>
            <h1 style='color: red'>Good Bye !!</h1>
            <p>Departure:</p>
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmVsMmIxaWVjaHF1NHdkZTB3cTdnbjVta3BjN25vZWV2aGpiM2E0NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W307DdkjIsRHVWvoFE/giphy.gif" width=300>
        </body>
    </html>
    '''

@app.route('/<num>')
def index(num):
    return f'The square of {num} is {int(num) ** 2}'


if __name__ == '__main__':
    app.run(debug=True)