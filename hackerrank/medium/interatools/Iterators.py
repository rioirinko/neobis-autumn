from itertools import combinations
N = int(input())
a = input().split()
K = int(input())
lst = list(combinations(a, K))
fil = filter(lambda c: 'a' in c, lst)
print("{0:.3}".format(len(list(fil))/len(lst)))
