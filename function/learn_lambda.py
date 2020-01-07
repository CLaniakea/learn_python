def build(x, y):
    return lambda: x * x + y * y
def build2(x,y):
    return x*x + y*y

print(build(1,2)())
print(build2(1,2))

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
X = list(filter(lambda n: n%2==1,range(1,20)))
print(L)
print(X)
