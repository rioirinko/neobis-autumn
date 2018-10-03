def split_and_join(line):
    line = "-".join(line.split())
    return(line)
line = input()
result = split_and_join(line)
print(result)
