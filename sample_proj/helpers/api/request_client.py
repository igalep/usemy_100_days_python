import json
import requests

JSON_CONTENT_TYPE = 'application/json'


def _prepare_headers(headers):
    return headers if headers else {'Content-Type': 'application/json'}

def _get_response_content(response):
    if JSON_CONTENT_TYPE in response.headers.get('Content-Type', ''):
        # Safely parse the JSON data
        return response.json()
    else:
        return response.text


def post(url, payload=None, headers=None, expected_status_code=201):
    """
    Send a POST request to the specified url with the given payload and headers. Asserts
    that the response status code matches the expected value. Returns the JSON response content.
    """
    headers = _prepare_headers(headers)

    response = requests.post(url=url, data=json.dumps(payload), headers=headers)
    assert response.status_code == expected_status_code, \
        f'Expected status code: {expected_status_code}, but got: {response.status_code}'

    return _get_response_content(response)


def get(url, expected_status_code=200, headers=None,  **kwargs):
    """
    Sends a GET request to the specified API url with optional parameters,
    validates the response status code, and returns the JSON-formatted response data.
    """
    headers = _prepare_headers(headers)

    response = requests.get(url=url, params=kwargs, headers=headers)

    assert response.status_code == expected_status_code, \
        f'Expected status code: {expected_status_code}, but got: {response.status_code}'

    return _get_response_content(response)



def put(url, payload=None, headers=None, expected_status_code=200):
    """
    Sends an HTTP PUT request to the specified url with the provided payload and
    headers. This function asserts that the response's status code matches the expected
    status code. The response body is returned as JSON.
    """
    headers = _prepare_headers(headers)

    response = requests.put(url=url, data=json.dumps(payload), headers=headers)
    assert response.status_code == expected_status_code, \
        f'Expected status code: {expected_status_code}, but got: {response.status_code}'

    return _get_response_content(response)


def delete(url, headers=None, expected_status_code=200):
    """
    Send a DELETE HTTP request to the specified url using the provided headers
    and compare the response status code with the expected status code. Ensures
    that the server response matches the expectation before proceeding.
    """
    response = requests.delete(url=url, headers=headers)
    assert response.status_code == expected_status_code, \
        f'Expected status code: {expected_status_code}, but got: {response.status_code}'

    return  'Deleted successfully'