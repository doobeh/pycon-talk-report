import csv
from collections import namedtuple
import requests
from bs4 import BeautifulSoup
import os
from collections import Counter
import yaml

config = yaml.load(file('config.yaml'))

reviewers = list()

for talk in os.listdir(config["save_path"]):
    with file(os.path.join(config["save_path"], talk)) as f:
        soup = BeautifulSoup(f)
        reviews = soup.find_all(attrs={'class': 'review-content'})
        for review in reviews:
            reviewers.append(review.b.text)

c = Counter(reviewers)
for user, occurences in c.most_common():
    print '{} : {}'.format(occurences, user.encode('utf8'))