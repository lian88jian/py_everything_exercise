import time

time.sleep(1)
print('1')
time.sleep(1)
print('2')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))