
a = 'abcdefg';
b = 'abef';

index = 0;
for chr in b:
    index = a[index:].find(chr)
    if index < 0:
        break;
        
print(index)