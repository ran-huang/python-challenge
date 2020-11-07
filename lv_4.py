import urllib.request
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
nothing = str(16044/2)
while True:
    html = urllib.request.urlopen(uri % nothing).read().decode()
    print(html)
    match = re.search("and the next nothing is (\d+)",html)
    if match == None:
        break
    nothing = match.group(1)
