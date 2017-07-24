#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import requests
import argparse
import datetime
from config import api_key


def check_date(ph_date):
    try:
        datetime.datetime.strptime(ph_date, '%Y-%m-%d')
        return True
    except ValueError:
        print("Incorrect date format./nSpecify a date in format: YYYY-MM-DD")
        return False


def show_photo(ph_date=''):
    ap_data = apod_get_json(api_key, ph_date)
    if ap_data:
        if option['hires']:
            print(ap_data['hdurl'])
        else:
            print(ap_data['url'])
        if option['info'] or option['title']:
            print(ap_data['title'])
        if option['info'] or option['expl']:
            print(ap_data['explanation'])
        if option['info']:
            print(ap_data['date'], '/', ap_data['media_type'])


def apod_get_json(api_key, ph_date=''):
    base_url = "https://api.nasa.gov/planetary/apod"
    r = requests.get("%s?api_key=%s&date=%s" % (base_url, api_key, ph_date))
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        print('bad status code:', r.status_code)
        return False


parser = argparse.ArgumentParser(description='NASA: Astronomy Photo Of the Day (APOD)')
parser.add_argument('--date','-d', action="store", help='the date of the APOD image retrive')
parser.add_argument('--hires','-r', action='store_true', default=False, help='show the link to the photo in high resolution')
parser.add_argument('--info','-i', action="store_true",  help='show full information about media')
parser.add_argument('--title','-t', action="store_true", help='show photo title')
parser.add_argument('--expl','-e', action="store_true", help='show explanation text')

args = parser.parse_args()
option = vars(args)

if option['date']:
    if check_date(option['date']):
        show_photo(ph_date=option['date'])
else:
    show_photo()
