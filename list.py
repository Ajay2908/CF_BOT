import data_fetcher as data
import os
import requests
import json


def upcoming_list():
    list = data.get_list()
    json_objects = []
    for items in list:
        json_data = requests.get(items)
        parsed_json = (json.loads(json_data.text))
        json_objects.append(parsed_json)

    contests_list = []
    for objects in json_objects:
        for contests in objects['objects']:
            contests_list.append(contests)

    return contests_list
