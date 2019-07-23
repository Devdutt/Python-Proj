import sys
import os
import requests
import math

print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com")
print(r.status_code)


rate = input('What is the job rate? ')
hours = input('How many hours per week? ')
pay = float(rate) * float(hours)
print('The pay is: ' + '$' + str(pay))
