import pprint

import requests

MY_LAT = 36.443241
MY_LNG = 28.227011

API_KEY = '8cc36dcb109ff69b94b138a0bc1c8003'


def get_weather_lat_lng(endpoint, **kwargs):
    url = f'https://api.openweathermap.org/data/2.5/{endpoint}'
    param = {
        'lat' : MY_LAT,
        'lon' : MY_LNG,
        'appid' : API_KEY,
        'units' : 'metric'
    }

    param.update(kwargs)

    response = requests.get(url=url , params=param)
    data = response.json()

    weather_code = [entry['weather'][0]['id'] for entry in data['list']]

    print(weather_code)
    weather_code.sort(reverse=True)
    if weather_code[0] > 800:
        print("Rain")



# get_weather_lat_lng(endpoint='weather')
params = {
    'cnt' : 24
}
get_weather_lat_lng(endpoint='forecast', **params)
