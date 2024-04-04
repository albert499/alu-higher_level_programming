#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
"""
import requests

if _name_ == '_main_':
    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = "https://alu-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
