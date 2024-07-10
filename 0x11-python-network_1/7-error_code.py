#!/usr/bin/python3
"""
    a Python script that takes in a URL
    - sends a request to the URL and displays the
    body of the response.
"""
if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(e)
