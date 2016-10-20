

def fn(n):
    if n == 1: return 10;
    return fn(n - 1) + 2;

print(fn(5))