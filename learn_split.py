

def trim(s):
    while s[0:1]==' ':
        s = s[1:]
    while s[-2:-1]==' ':
        s = s[:-2]
    return s

s='    '
print(trim(s))