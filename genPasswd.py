#!/usr/bin/python3

import secrets
import string

if __name__ == "__main__":
    lunghezza = "x"
    while (not lunghezza.isdigit()):
        lunghezza = input('Numero di caratteri: ')
    alphabet = string.ascii_letters + string.digits + string.punctuation
    for i in range(5):
        password = ''.join(secrets.choice(alphabet) for i in range(int(lunghezza)))
        print('Password (' + str(i+1) + '): ' + password)
