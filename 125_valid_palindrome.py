import re

s = input()
s = s.lower()
s = re.sub('[^a-zA-Z0-9_]+', '', s)
ns = list(s)
ns.reverse()
ns = "".join(ns)
if s == ns:
    print(True)
else:
    print(False)
