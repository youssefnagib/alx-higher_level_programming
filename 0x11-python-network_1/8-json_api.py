#!/usr/bin/python3
"""
     a Python script that takes in a letter
     and sends a POST request to http://0.0.0.0:5000/search_user
     with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        r = response.json()
        if r == "":
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
