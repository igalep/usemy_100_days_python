from sample_proj.helpers.vault.vault_access import VaultAccess
import json
import requests


class BaseClient:
    def __init__(self):
        self.vault = VaultAccess()
        self.api_key = ''
        self.data = ''


    def get_api_key(self):
        vault_secrets = self.vault.pull_data(**self.data).get('data', {}).get('data', {})
        self.api_key = vault_secrets['api_key']

        print(f'api_key = {self.api_key}')
        pass

    def get(self, url,**kwargs):
        api_res = requests.get(url=url, params=kwargs)
        # pprint.pprint(api_res.json())
        return api_res.json()

    def post(url, payload=None, headers=None, expected_status_code=200):
        """
        Sends a POST request to a given URL with the provided payload and headers. It
        validates that the response status code matches the expected status code and
        returns the JSON response body.

        :param url: The endpoint URL to make the POST request to.
        :type url: str
        :param payload: The data to be included in the request body. Defaults to None.
        :type payload: dict or None
        :param headers: The HTTP headers to be included in the request. Defaults to
            {'Content-Type': 'application/json'} if not provided.
        :type headers: dict or None
        :param expected_status_code: The HTTP status code expected from the response.
            Defaults to 200.
        :type expected_status_code: int
        :return: The JSON-decoded response body.
        :rtype: dict
        """
        print(f'URL --->: {url}')

        if not headers:
            headers = {'Content-Type': 'application/json'}

        rs_api = requests.post(url=url, data=json.dumps(payload), headers=headers)
        status_code = rs_api.status_code
        assert status_code == expected_status_code, \
            f'Expected status code: {expected_status_code}, but got: {status_code}'

        # logging.error(f'API Response: {rs_api.content}')

        # logging.debug(curlify.to_curl(rs_api.request))

        return rs_api.json()

