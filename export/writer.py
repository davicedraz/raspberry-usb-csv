import json
import csv

from config import config as env

def write_header(dict):
    try:
        reader = csv.reader(open(env.FILE_PATH, newline=''))

    except FileNotFoundError:
        writer = csv.writer(open(env.FILE_PATH, 'w'))
        signals_keys = []
        for key, value in dict.items():
            signals_keys.append(key)

        writer.writerow(signals_keys)


def write_data(payload):
    writer = csv.writer(open(env.FILE_PATH, 'a'))

    values = []
    for key, value in payload.items():
        values.append(value)

    writer.writerow(values)
