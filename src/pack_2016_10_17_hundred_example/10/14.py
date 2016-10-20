

#分解质因数
num = 90;
primeArr = [];
i = 2;
while i <= num:
    if num % i == 0:
        primeArr.append(i);
        num /= i;
    else:
        i += 1;
for i in range(len(primeArr)):
    if i == 0:
        print('%d' % primeArr[i],end="");
    else:
        print(' * %d' % primeArr[i],end="");
        