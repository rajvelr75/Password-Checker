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

def get_leak_count(hashes,hashes_to_check):
    # Received response from the API will be in a list[remaining characters that needed to be checked : count of times the hash found]
    recived_hash = (line.split(':') for line in hashes.text.splitlines())
    for h, count in recived_hash:
        # spliting hash and count recived from the api
        if h == hashes_to_check:

            return count
def pwned_api_check(password):
    #hashing the password
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    #Splitting the Password
    first_5,tail = sha1password[:5],sha1password[5:]

    #requesting Api with first five Characters
    response = req_api_data(first_5)

    #receiving response and getting count
    return get_leak_count(response,tail)




