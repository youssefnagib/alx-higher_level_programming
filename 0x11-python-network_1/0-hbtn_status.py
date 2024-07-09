#!/usr/bin/python3
"""
    _A Python script that fetches https://alx-intranet.hbtn.io/status_
"""

import urllib.request


if __name__ == "__main__":
    import urllib
    
    with urllib.request.urlopen("http://alx-intranet.hbtn.io/status") as url:
        response = url.read()
        print("Body response:")
        print("/t- type: {}".format(type(response)))
        print("/t- content: {}".format(response))
        print(" /t- uyf8 content: {}".format(response.decode('utf8')))