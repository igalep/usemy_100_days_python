import json
import pprint

import requests


def post(url, payload=None, headers=None, expected_status_code=200):
    """
    Sends a POST request to a given URL with the provided payload and headers. It
    validates that the response status code matches the expected status code and
    returns the JSON response body.
    """
    print(f'URL --->: {url}')

    if not headers:
        headers = {'Content-Type': 'application/json'}
    else:
        headers.update({'Content-Type': 'application/json'})

    rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers)
    status_code = rs_api.status_code
    assert status_code == expected_status_code, \
        f'Expected status code: {expected_status_code}, but got: {status_code} \
        and the error is {rs_api.text}'

    # logging.error(f'API Response: {rs_api.content}')

    # logging.debug(curlify.to_curl(rs_api.request))

    return rs_api.json()


def get(url,**kwargs):
    """
    Sends a GET request to the specified URL with provided keyword arguments and
    prints the JSON response content.

    This function utilizes the requests library to send the GET request
    and pprint for pretty-printing the JSON response. It allows passing
    additional parameters for customization of the HTTP request through
    keyword arguments.
    """
    api_res = requests.get(url=url,params=kwargs)

    pprint.pprint(api_res.json())