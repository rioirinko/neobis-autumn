from collections import deque
for _ in range(int(input())):
    n = int(input())
    t = deque(list(map(int, input().split())))
    if t[0] > t[-1]: s = t.popleft()
    else: s = t.pop()
    while(len(t) > 0):
        if t[0] >= t[-1] and t[0] <= s:
            s = t.popleft()
        elif t[-1] >= t[0] and t[1] <= s:
            s = t.pop()
        else:
            break
    print("Yes" if len(t) == 0 else "No")
