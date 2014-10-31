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

Create a virtualenv, activate it and install the requirements:

    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

Copy `config-example.yaml` to `config.yaml` and fill in your private
details and the location where you'd like to save the talks to.