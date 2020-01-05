from functools import reduce
'''
def f(x):
    return x*x
s = [1,2,3,4,5,6,7,8,9]
r = map(f,s)
L = map(str,s)
print(type(s))

print(list(r))
print(list(L))
print(type(list(L)))
print(list(L))

def add(x,y):
    return x*10 + y

s = [1, 3, 5, 7, 9]
d = reduce(add,s)
print(d)
print(type(d))

ls = [1, 2, 3]
print(ls)
print(type(ls))
print(list(ls))
print(list(ls))
'''
'''
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def f(x, y):
        return x*10+y
    def char2num(s):
        return digits[s]
    return reduce(f,map(char2num,s))
    # map works char of s to list of s
    # reduce works list of s to int
s = '123456'
print(type(s))
print(str2int(s))
print(type(s))
'''

# example 1
'''
def normalize(name):
    temp=''
    s = name[0:1].upper()
    temp = temp + s
    s = name[1:].lower()
    temp = temp + s
    return temp
s = 'aaa'
print(normalize(s))
'''

# example 2
'''
def prod(L):
    def f(x,y):
        return x*y
    ret = reduce(f,L)
    return ret
L=[3,5,7,9]
print(prod(L))
'''

# example 3
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    L = s.split('.')
    count = len(L[1])
    s = L[0] + L[1]
    def f(x, y):
        return x*10+y
    def char2num(s):
        #count = count - 1
        return digits[s]
    ret = reduce(f,map(char2num,s))
    return ret /(10 ** count)
#print(str2float('123.456'))
s='123.456'
print(s.find('.'))