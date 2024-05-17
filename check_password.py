import requests
import hashlib
import sys 


def req_api_data():
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error {res.status_code}")
    else:
        return res
req_api_data()