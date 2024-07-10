#!/usr/bin/python3
"""
    - a Python script that takes in a URL
    - sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
if __name__ == '__main__':
    from urllib import request, error
    import sys

    url = sys.argv[1]
    try:
        request = request.Request(url)

        with request.urlopen(request) as response:
            body = response.read().decode('utf-8')
            print(body)
    except error.HTTPError as error:
        print(f"Error code: {error.code}")
