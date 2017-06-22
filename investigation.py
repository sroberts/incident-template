#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import json

token = os.environ['GH_TOKEN']

project = "sroberts/test"
project_url = "https://api.github.com/repos/{}/projects".format(project)

def main():
    print("Setting Up Project: {}".format(project_url))

    h = {'Authorization': 'token {}'.format(token), 'Accept': 'application/vnd.github.inertia-preview+json'}

    project_systems_triage = {
          "name": "System Triage",
          "body": "To be triaged, analyzed, remedated, and returned to service."
    }

    r = requests.post(project_url, headers=h, data=json.dumps(project_systems_triage))

    print(r.text)

if __name__ == '__main__':
    main()
