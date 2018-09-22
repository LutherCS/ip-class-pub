#!/usr/bin/env python3

import cgi
from datetime import datetime as dt


def isPrime(n: int) -> bool:
    '''Check if the number is prime'''
    for i in range (2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

params = cgi.FieldStorage()
name = params['name'].value
n = int(params['n'].value)

print('Content-Type: text/html')
print()

print('<html>')
print('  <head>')
print('    <title>Hello CS330</title>')
print('  </head>')
print('  <body>')
print('<h1>Hello {}!</h1>'.format(name))
print('<p>Today is <em>{}</em></p>'.format(dt.now()))
if isPrime(n):
    print('{} is prime'.format(n))
else:
    print('{} is NOT prime'.format(n))
print('  </body>')
print('</html>')
