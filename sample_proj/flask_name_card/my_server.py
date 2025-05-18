from flask import Flask, render_template
from concurrent.futures import ThreadPoolExecutor
import datetime
import requests

app = Flask(__name__)
executor = ThreadPoolExecutor(max_workers=2)

@app.route('/')
def foo():
    json_body = {
        'name': 'John Doe',
        'age': 30,
    }
    return json_body


def fetch_data(url, params):
    try:
        response = requests.get(url=url, params=params, timeout=3)
        response.raise_for_status()

        return response.json()
    except requests.RequestException as e:
        app.logger.error(f'There were an exception in request to {url} ---> {e}')
        return None

@app.route('/name/<input_name>')
def name(input_name):
    url_age = 'https://api.agify.io'
    url_gender = 'https://api.genderize.io'
    params = {
        'name': input_name,
    }

    age_data = executor.submit(fetch_data, url=url_age, params=params)
    gender_data = executor.submit(fetch_data, url=url_gender, params=params)

    age = age_data.result().get('age', None)

    gender = gender_data.result().get('gender', None)
    probability = gender_data.result().get('probability', None)


    this_year = datetime.datetime.now().year
    return render_template('index.html', year=this_year,
                           name = input_name.capitalize(), age=age, gender=gender, probability=probability)


if __name__=='__main__':
    app.run(debug=True)