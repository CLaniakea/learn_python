'''
def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3

for o in odd():
    print(o)
'''
'''
def fib(max):
    n,a,b=0,0,1
    while n < max:
        yield b
        a,b=b,a+b
        n = n + 1
    return 'done'
f=fib(6)
while True:
    try:
        x = next(f)
        print('f:',x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break
'''
# way 1 ,hard way
def triangles():
    L = []
    L1 = [1]
    n = 0
    now=1
    while True:
        if n==1:
            L1=[1,1]
        elif n > 1:
            L1.append(1)
            while now < n:
                temp = L[now-1]+L[now]
                L1.append(temp)
                now=now+1
            L1.append(1)
        yield L1
        L=L1
        L1=[]
        now=1
        n=n+1
# for t in triangles(10):
#     print(t)
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

# way 2 ,elegant, waiting...