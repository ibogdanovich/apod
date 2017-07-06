import requests
import argparse
from config import api_key


def apod_get_json(base_url, api_key):
    r = requests.get("%s?api_key=%s" % (base_url,  api_key))
    if r.status_code == 200:
        return r.json()
    else:
        print('bad status code:', r.status_code)


def apod_get_image(url):
    r = requests.get(url)
    if r.status_code == 200:
        with open('/home/ibd/afod_img/asod.jpg', 'wb') as f:
            f.write(r.content)
        return True


parser = argparse.ArgumentParser(description='NASA: Astronomy Photo Of the Day (APOD)')
parser.add_argument('--hd', action='store_true', default=False, help='Show APOD in HD URL')
# parser.add_argument('--title', help='Show APOD title')
# parser.add_argument('--expl', help='Show APOD explanation text')
parser.add_argument('--date', help='requested date')
args = parser.parse_args()
options = vars(args)
base_url = "https://api.nasa.gov/planetary/apod"

ap_data = apod_get_json(base_url, api_key)

print(ap_data['title'], '\n')
print(ap_data['date'], ap_data['media_type'])
print(ap_data['explanation'])
print(ap_data['hdurl']) if options['hd'] else print(ap_data['url'])
