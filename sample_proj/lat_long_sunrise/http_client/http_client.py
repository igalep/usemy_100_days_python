import requests

def get(endpoint, **kwargs):
    response = requests.get(url=endpoint,params=kwargs)
    response.raise_for_status()

    return response.json()