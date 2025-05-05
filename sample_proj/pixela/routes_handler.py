import random
from sample_proj.helpers.api.request_client import post
from datetime import datetime , timedelta

# my graph at https://pixe.la/v1/users/igalep/graphs/graph1.html

BASE_URL = "https://pixe.la"

USERNAME = 'igalep'
TOKEN = 'igalep0802'

HEADERS = {
    'X-USER-TOKEN': TOKEN
}

GRAPH_ID = 'graph1'


def create_user():
    route = '/v1/users'

    user_params = {
        'token' : TOKEN,
        'username' : USERNAME,
        'agreeTermsOfService' : 'yes',
        'notMinor' : 'yes'
    }

    response = post(f'{BASE_URL}{route}', payload=user_params)

    print(response)


def create_graph(username):
    route = f'/v1/users/{username}/graphs'

    graph_config = {
        'id' : GRAPH_ID,
        'name' : 'Udemy Coding Graph',
        'unit' : 'Hours',
        'type' : 'float',
        'color' : 'momiji'
    }

    response = post(f'{BASE_URL}{route}', payload=graph_config, headers=HEADERS)

    print(response)

def generate_pixel_collection(username, graph_id):
    pixel_arr = []
    for i in range(1, 11):
        pixel_params = {
            'date': datetime.now().date().strftime("%Y%m%d"),
            'quantity': f'{i * random.random()}'
        }
        pixel_arr.append(pixel_params)

        return pixel_arr

def post_pixel(username, graph_id, quantity):
    route = f'/v1/users/{username}/graphs/{graph_id}'

    pixel_params = {
        'date' : (datetime.now().date() - timedelta(days=3)).strftime("%Y%m%d"),
        'quantity' : f'{quantity}'
    }
    response = post(f'{BASE_URL}{route}', payload=pixel_params, headers=HEADERS)

    print(response)

def post_pixel_multiple(username, graph_id,):
    route = f'/v1/users/{username}/graphs/{graph_id}/pixels'

    pixels = generate_pixel_collection(username, graph_id)

    response = post(f'{BASE_URL}{route}', payload=pixels, headers=HEADERS)

    print(response)


# create_user()
# create_graph(username=USERNAME)
post_pixel(username=USERNAME, graph_id=GRAPH_ID, quantity=4.5)

# post_pixel_multiple(username=USERNAME, graph_id=GRAPH_ID)