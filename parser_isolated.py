"""
Processes the PyCon Talk downloads to count the active votes per person.  If a user
has voted more then once on a talk, it only counts the latest vote.
"""

from bs4 import BeautifulSoup
import os
from collections import Counter
import yaml

config = yaml.load(file('config.yaml'))

reviewers = list()

for talk in os.listdir(config["save_path"]):
    #print "Processing {}".format(talk)
    with file(os.path.join(config["save_path"], talk)) as f:
        soup = BeautifulSoup(f)
        reviews = soup.find_all(attrs={'class': 'review-box'})

        reviewed = list()
        for review in reviews:
            rating = review.find(attrs={'class': 'vote'}).span.text
            reviewer = review.find(attrs={'class': 'review-content'}).b.text
            if reviewer not in reviewed:
                if len(rating):  # Exclude reviews without a vote.
                    reviewed.append(reviewer)
                    reviewers.append(review.b.text)

c = Counter(reviewers)
for user, occurrences in c.most_common():
    print '{} : {}'.format(occurrences, user.encode('utf8'))