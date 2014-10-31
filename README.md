Pycon Talk Report
=================

Just a simple downloader that allows PyCon program committee users to download
all the available talks so they can refer to them offline.

It also includes a little script `parser_isolated.py` that will do a quick
ranking report showing how many votes per active reviewer.  `parser.py`
will show a ranking report of all comments (reviews included) posted per
user.

Installation
============

Create a virtualenv, and install the requirements `pip install -r requirements.txt`
and then copy `config-example.yaml` to `config.yaml` and fill in your private
details and local filesystem location for saving the talks.