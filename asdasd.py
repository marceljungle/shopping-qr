import urllib.request
import json
with urllib.request.urlopen("http://google.com/json?address=google") as url:
    data = json.loads(url.read().decode())
    print(data)
