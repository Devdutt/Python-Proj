import sys
import os
import requests
import math


print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com")
print(r.status_code)

# end comment
