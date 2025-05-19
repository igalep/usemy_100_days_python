from flask import Flask, render_template
import requests


app = Flask(__name__)



blog_data = None
def get_blogs():
    url = 'https://api.npoint.io/bf562e52ffd4e3c69384'

    global blog_data
    if blog_data is None:
        blog_data = fetch_data(url=url)

    return blog_data


@app.route('/')
def home():
    posts = get_blogs().get('blog_posts')
    return render_template('index.html', posts=posts)

@app.route('/post/<int:blog_id>')
def read_blog(blog_id):
    return render_template('post.html', post = get_blogs().get('blog_posts')[blog_id - 1])

def fetch_data(url, params=None):
    try:
        response = requests.get(url=url, params=params, timeout=3)
        response.raise_for_status()

        return response.json()
    except requests.RequestException as e:
        app.logger.error(f'There were an exception in request to {url} ---> {e}')
        return None

if __name__ == "__main__":
    app.run(debug=True)
