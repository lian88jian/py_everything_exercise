from pip._vendor.distlib.compat import raw_input

ratioArr = [
        {
            'num':1000000,
            'ratio':0.01
        },
        {
            'num':600000,
            'ratio':0.015
        },
        {
            'num':400000,
            'ratio':0.03
        },
        {
            'num':200000,
            'ratio':0.05
        },
        {
            'num':100000,
            'ratio':0.075
        },
        {
            'num':0,
            'ratio':0.1
        }
]
num = int(raw_input());
sum = 0;
for ratio in ratioArr:
    if num > ratio['num']:
        sum += ratio['ratio'] * (num - ratio['num']);
        print(ratio['ratio'] * (num - ratio['num']))
        num = ratio['num'];

print(sum)