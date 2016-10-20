from pip._vendor.distlib.compat import raw_input


def fn(n):
    if n == 5: return ;
    num = raw_input('no.%d:' % n);
    n += 1;
    fn(n);
    print(num);
    
def res(str, index = 0):
    if len(str) == index: return ;
    i = index + 1;
    res(str, i);
    print(str[index],end='');
    
# fn(0);
res('abcdef')
