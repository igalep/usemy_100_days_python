import pprint

from .http_client import get


class Nasa:
    def __init__(self):
        self.BASE_URL = 'http://api.open-notify.org/'


    def get_location(self):
        endpoint = f'{self.BASE_URL}iss-now.json'
        location = get(endpoint=endpoint)

        # pprint.pprint(location)
        return location

    def get_people_in_space(self):
        endpoint = f'{self.BASE_URL}astros.json'
        personal = get(endpoint=endpoint)

        pprint.pprint(personal)


# n = Nasa()
# n.get_location()
# n.get_people_in_space()
