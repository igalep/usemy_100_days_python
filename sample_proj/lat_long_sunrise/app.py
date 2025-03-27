from http_client.sun_time import SunTimes
from http_client.nasa_location import Nasa
from datetime import datetime

LAT = 32.164860
LNG = 34.844170

def is_overhead():
    nasa_location = Nasa()
    current_location = nasa_location.get_location()

    current_lat = current_location['iss_position']['latitude']
    current_lng = current_location['iss_position']['longitude']

    if LAT - 5 <= float(current_lat) <= LAT + 5:
        if LNG - 5 <= float(current_lng) <= LNG + 5:
            return True

    return False

def is_night():
    sun_time = SunTimes()
    sunrise_sunset = sun_time.get_sunrise_sunset()

    now = datetime.now().hour
    if now < sunrise_sunset[0] or now > sunrise_sunset[1]:
        return True

def app():
    overhead = is_overhead()
    night = is_night()
    print(f'You can see the nasa above you right now: {overhead and night}\noverhead =  {overhead} and dark = {night}')








def main():
    app()




if __name__ == '__main__':
    main()