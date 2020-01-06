'''
def is_odd(x):
    return x % 2 == 1

L = [1,2,3,4,5,6,7,8,9]
print(list(filter(is_odd,L)))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['a', '', 'c'])))
'''

def is_palindrome(x):
    s = 0
    source = x
    while x > 0.1:
        temp = x % 10
        x = int(x / 10)
        s = s * 10 + temp
    if source == s:
        ret = True
    else:
        ret = False
    return ret
print(list(map(is_palindrome,range(1, 1000))))