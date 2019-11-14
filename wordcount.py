import string
from collections import Counter
f = open("mytext.txt", "r")
tekst = f.read()

k = tekst.split()

newlines = []
for item in k:
   newlines.append(item.strip(string.punctuation))
k = newlines
#print(k)
c = Counter(k)
#print(c)
#print(c.most_common())

for m, n in c.most_common():
    print ("{} {}" .format(m, n))

