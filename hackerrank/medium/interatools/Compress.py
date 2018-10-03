from itertools import groupby
s = input()
for a, b in groupby(s):
    print(tuple((len(list(b)),int(a))),end=' ')
