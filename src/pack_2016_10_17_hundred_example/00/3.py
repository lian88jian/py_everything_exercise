'''
Created on 2016年10月17日

@author: lianjian
'''
import math

for i in range(1,100000):
    x = math.sqrt(i + 100)
    y = math.sqrt(i + 268)
    if x - int(x) == 0 and y - int(y) == 0:
        print(i)