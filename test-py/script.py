import sys
from os import rename
import requests
import math

print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com")
print(r.status_code)

""" maxChar = max(input("Please type some words: "))
print(maxChar) """

smallest = None
print(smallest)
setOfNumbers = [23, 3091, 3, 55, 9, 0, 8, 76, 900]

for i in setOfNumbers:
    if smallest == None:
        smallest = i
    print(i)
    if i < smallest:
        smallest = i

print("The Smallest Number is ", smallest)
# Add comments here.....
