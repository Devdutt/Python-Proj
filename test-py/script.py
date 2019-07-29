import sys
import os
import requests
import math

print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com")
print(r.status_code)

""" maxChar = max(input("Please type some words: "))
print(maxChar) """

l_number = -1
print(l_number)
setOfNumbers = [23, 3091, 3, 55, 9, 0, 8, 76, 900]

for i in setOfNumbers:
    if i > l_number:
        l_number = i
        print("largest Number so far is ", l_number)

print("Done! the largest number is", l_number)

# Add comments here.....
