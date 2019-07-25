import sys
import os
import requests
import math

print(sys.version)
print(sys.executable)
""" 
r = requests.get("https://www.google.com")
print(r.status_code)


rate = input('What is the job rate? ')
hours = input('How many hours per week? ')
pay = float(rate) * float(hours)

if pay < 5000:
    print('The pay is: ' + '$' + str(pay))
elif pay > 5001:
    print('This pay is higher than $5001.00' + str(pay)) """

maxChar = max(input("Please type some words: "))
print(maxChar)
