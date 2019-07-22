import sys
import os
import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://www.google.com")

print(r.status_code)
# end comment
