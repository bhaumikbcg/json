import json
import urllib.request, urllib.parse, urllib.error

url = input('url')
html = urllib.request.urlopen(url).read()
info = json.loads(html.decode("utf-8"))
print ('User count:', len(info["comments"]))
num = 0
comments = info["comments"]
for comment in comments:
    num = num + comment["count"]
print (num)