


num = 51234543215;
num = str(num);
isOrNot = True;
for i in range(int(len(num) / 2)):
#     print('%s == %s ? %s' % (num[i], num[len(num) - i - 1], num[i] == num[len(num) - i - 1]))
    if num[i] != num[len(num) - i - 1]:
        isOrNot = False;
        break;

if isOrNot == False:
    print("no!");
else:
    print("yes!");