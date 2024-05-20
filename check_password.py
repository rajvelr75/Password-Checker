import requests
import hashlib
import sys 


def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error {res.status_code}")
    else:
        return res

def get_leak_count():
    pass
def pwned_api_check(password):
    #hashing the password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #Splitting the Password
    first_5,tail = sha1password[:5],sha1password[5:]
    response = req_api_data(first_5)
    return get_leak_count(response,tail)

pwned_api_check()



