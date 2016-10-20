

numArr = [1, 2];
for i in range(2,21):
    numArr.append(numArr[i - 2] + numArr[i - 1]);

sum = 0;
for i in range(1,len(numArr)):
    sum += numArr[i] / numArr[i - 1]
#     print('%d / %d' % (numArr[i], numArr[i - 1]) )
print(sum);