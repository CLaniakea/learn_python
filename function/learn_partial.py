import functools
int2 = functools.partial(int, base = 10)
print(int2('500'))