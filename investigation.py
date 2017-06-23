#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import json
import random

token = os.environ['GH_TOKEN']

server = "https://api.github.com"
project = "sroberts/test"

h = {
    'Authorization': 'token {}'.format(token),
    'Accept': 'application/vnd.github.inertia-preview+json'
}

words = open('/usr/share/dict/words').readlines()

def generate_codename():
    return "{}-{}".format(random.choice(words).strip(), random.choice(words).strip())

def create_board(name, body, columns=[]):
    """Creates a GitHub Project Board"""

    project_url = "{}/repos/{}/projects".format(server, project)

    board_content = json.dumps({
        "name": name,
        "body": body
    })

    try:
        r = requests.post(project_url, headers=h, data=board_content)
        html_url = r.json()['html_url']
        board_id = r.json()['id']
    except:
        raise

    print("Created board {}: {}".format(name, html_url))

    for column in columns:
        print("  - Creating column: {}".format(column))

        url = "{}/projects/{}/columns".format(server, board_id)
        column = json.dumps({"name": column})

        try:
            r = requests.post(url, headers=h, data=column)
        except:
            raise

    return html_url


def main():
    """Where the business ets done"""
    print("Setting Up Project: {}".format(project))

    setup = json.loads(open('setup.json', 'r').read())

    for board in setup:
        create_board(board['name'], board['description'], board['columns'])

if __name__ == '__main__':
    main()
