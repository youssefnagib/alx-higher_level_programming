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
        print("    - type: {}".format(type(response)))
        print("    - content: {}".format(response))
        print("    - utf8 content: {}".format(response.decode('utf8')))
