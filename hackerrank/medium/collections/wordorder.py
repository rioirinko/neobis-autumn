from collections import OrderedDict
n = int(input())
k = OrderedDict()

for _ in range(n):
    new_word=input()
    if new_word in k:
        k[new_word] += 1
    else:
        k[new_word] = 1

print(len(k))
print(*k.values())
