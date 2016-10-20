
def check_string_contain(str, subStr, test=False):
    str = str.lower().replace('spanclassemojiemoji','').replace('span','');
    index = 0;
    for chr in subStr:
        i = str[index:].find(chr)
        if test:
            print(index)
        if i < 0:
            index = -1;
            break;
        index += i;
    return index != -1;

if __name__ == '__main__':
    str = 'spanclassemojiemoji274cspanspanclassemojiemoji2734span?spanclassemojiemoji1f49fspan?gaweicm7993';
    subStr = 'moniao';
    print(check_string_contain(str, subStr, test=True));
    
    print('monia' in 'moniao')