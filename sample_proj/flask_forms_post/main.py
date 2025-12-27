from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def foo():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def post_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # return render_template('login.html', username=username, password=password)
        return f'<h1>Your user name is : {username}, and password is : {password}</h1>'

    return 'Failed !!'


if __name__ == '__main__':
    app.run(debug=True)