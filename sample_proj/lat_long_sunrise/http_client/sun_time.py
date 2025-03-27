import pprint

from .http_client import get


class SunTimes:
    def __init__(self):
        self.BASE_URL = 'https://api.sunrise-sunset.org/json'
        self.lat_long_pos = {
            'lat' : 32.164860,
            'lng' : 34.844170,
            'formatted' : 0
        }


    def get_sunrise_sunset(self):
        sun_data = get(endpoint=self.BASE_URL, **self.lat_long_pos)
        # pprint.pprint(sun_data)

        time = (int(sun_data['results']['sunrise'].split('T')[1].split(':')[0]),
                int(sun_data['results']['sunset'].split('T')[1].split(':')[0]))

        # print(time)

        return time


# st = SunTimes()
# st.get_sun_status()

