#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import requests
import argparse
from config import api_key


def apod_get_json(base_url, api_key):
    r = requests.get("%s?api_key=%s" % (base_url,  api_key))
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print('bad status code:', r.status_code)


parser = argparse.ArgumentParser(description='NASA: Astronomy Photo Of the Day (APOD)')
parser.add_argument('--hires','-r', action='store_true', default=False, help='show the likt to the photo in high resolution')
parser.add_argument('--info','-i', action="store_true",  help='show full information about media')
parser.add_argument('--title','-t', action="store_true", help='show photo title')
parser.add_argument('--expl','-e', action="store_true", help='show explanation text')
args = parser.parse_args()
option = vars(args)
base_url = "https://api.nasa.gov/planetary/apod"

ap_data = apod_get_json(base_url, api_key)

print(ap_data['hdurl']) if option['hires'] else print(ap_data['url'])
if option['info'] or option['title']:
    print(ap_data['title'])
if option['info'] or option['expl']:
    print(ap_data['explanation'])
if option['info']:
    print(ap_data['date'], '/', ap_data['media_type'])

