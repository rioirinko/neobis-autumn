def merge_the_tools(string, k):
    l = len(string)//k
    for i in range(l):
        t = ''
        for c in string [i * k : i * k + k]:
            if c not in t: 
                t += c
        print(t)

string, k = input(), int(input())
merge_the_tools(string, k)
