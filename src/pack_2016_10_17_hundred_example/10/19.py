

for i in range(2, 1001):
    foctorArr = [];
    for j in range(1, i):
        if i % j == 0:
            foctorArr.append(j);
            
    sum = 0;
    for foctor in foctorArr:
        sum += foctor;
    if sum == i:
        print(i);
        print(foctorArr);