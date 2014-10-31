import csv
from collections import namedtuple
import requests
import os
import yaml

config = yaml.load(file('config.yaml'))

# Lets just dig through the csv file and pull out what we care about:
talk_urls = list()

with open(config["filename"]) as f:
    csv_reader = csv.reader(f)
    headings = ['id', 'speaker', 'title', 'category', 'tags', 'unused', 'A', 'B', 'C', 'D']
    _ = next(csv_reader)
    Row = namedtuple('Row', headings)
    for row in csv_reader:
        result = Row(*row)
        talk_urls.append({
            'url': config["talk_url"].format(talk_id=result.id),
            'id': result.id
        })


# And then download them onto our filesystem.
with requests.Session() as session:
    # hostname 'us.pycon.org' doesn't match either of '*.python.org', 'python.org'
    # so verify=False is required...?

    token_page = session.get(config["login_url"], verify=False)
    csrf_token = session.cookies["csrftoken"]

    payload = {
        'csrfmiddlewaretoken': csrf_token,
        'email': config["username"],
        'password': config["password"],
    }

    headers = {
        "X-CSRFToken": csrf_token,
        "Referer": config["login_url"],
    }

    cookies = dict(session.cookies)
    session.post(config["login_url"], data=payload, cookies=cookies, headers=headers)

    for talk in talk_urls:
        print 'Retrieving Talk ID: {}'.format(talk["id"])
        with file(os.path.join(config["save_path"], '{}.html'.format(talk["id"])), 'w') as f:
            f.write(session.get(talk["url"]).text.encode('utf8'))
