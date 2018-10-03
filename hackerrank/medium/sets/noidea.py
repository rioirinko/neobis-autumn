count = list(map(int, input().split()))
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
n = count[1]
m = count[0]
h = 0
for i in array:
    if i in A: 
        h += 1
    elif i in B: 
        h -= 1
print (h) 
