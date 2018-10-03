def count_substring(string, sub_string):
    j = 0
    for i in range(0,len(string)-2):
        s = string[i:i+len(sub_string)]
        if s == sub_string:
            j += 1
    return j
string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)    
