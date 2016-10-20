
def fn(n):
    if n == 1 or n == 0: return 1;
    return fn(n - 1) * n;
    
print(fn(5))
