'''
Created on 2016年10月17日

@author: lianjian
'''
from pip._vendor.distlib.compat import raw_input

l = [];
for i in range(1,4):
    l.append(int(raw_input('number_%d:' % i)));
l.sort();
print(l)
