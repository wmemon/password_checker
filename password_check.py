import requests
import hashlib
from collections import defaultdict
import getpass


def get_password():
    """
    The following function takes input without echo and hashes it to sha1 in Upper case.
    :library_used: hashlib,getpass
    :return: list of split hash into first five characters and rest.

    """
    password = getpass.getpass('Please enter a password:- ')
    if len(password) == 0:
        print("[!]Please enter a password.")
        exit(0)
    hashed_password =hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    five_char, tail = hashed_password[:5], hashed_password[5:]
    return([five_char,tail])


def get_result(five_char):

    """
    Uses the API to return result and convert to dictionary by string manipulation techniques.
    :library_used:requests
    :param five_char:
    :return:default dictionary d

    """

    res = requests.get(f'https://api.pwnedpasswords.com/range/{five_char}')
    if res.status_code != 200:
        return f"[!]Please check the API and the parameter given."
    diction = {}
    hashes = (i.split(':') for i in res.text.splitlines())
    for k, v in hashes:
        diction[k] = v
    d = defaultdict(lambda: "no", diction)
    return d

def in_result(default_dict,tail):
    """

    :param default_dict: The default dictionary from get_result()
    :param tail: the tail part result of get_password()
    :return: String telling the number of searches found.
    """
    if default_dict[tail] == "no":
        return f"The search returned no results. You are safe to use the password."
    return f"The search returned {default_dict[tail]} results. You are not safe. Please change your password."


