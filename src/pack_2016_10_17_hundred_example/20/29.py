


num = 52311;
numStr = str(num);

for i in range(len(numStr)):
    print(numStr[len(numStr) - i - 1],end='');
    
print('\n%d位数' % len(numStr))