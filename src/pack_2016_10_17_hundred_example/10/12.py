import math


def judge(n):
    for i in range(int(math.sqrt(n)), n):
        if n % i == 0: return False;
    return True;

for i in range(101,201):
    if judge(i):
        print(i);