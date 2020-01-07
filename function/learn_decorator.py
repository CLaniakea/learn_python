# PUZZLE
# PUZZLE
# PUZZLE

'''
def now():
    print('2015-3-25')
f = now
f()
print(f.__name__)
'''
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
'''
import time, functools
def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, func(*args, **kw)))
        return func(*args, **kw)
    return wrapper
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print(f,s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')