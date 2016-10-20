

def tripe(n):
    n = int(n);
    return n ** 3;

for i in range(100,1000):
    str = '%d' % i;
    if i == tripe(str[0]) + tripe(str[1]) + tripe(str[2]):
        print(i);
