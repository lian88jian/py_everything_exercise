'''
Created on 2016年10月5日

@author: lianjian
'''
from src.pack_2016_10_04_grayhat.chapter2.debugger_defines import *
class Debugger():
    
    def __init__(self):
        pass;
    
    def load(self,exePath):
        creation_flags = DEBUG_PROCESS;
        
        startupinfo = STARTUPINFO();
        startupinfo.dwFlags = 0x1;
        startupinfo.wShowWindow = 0x0;
        startupinfo.cb = sizeof(startupinfo);
        
        process_info = PROCESS_INFORMATION();
        
        if windll.kernel32.CreateProcessA(exePath,
                                          None,
                                          None,
                                          None,
                                          None,
                                          creation_flags,
                                          None,
                                          None,
                                          byref(startupinfo),
                                          byref(process_info)):
            print('We have successfully launched the process! processId:%s' % process_info.dwProcessId);
        else:
            print('Error: 0x%08x' % (windll.kernel32.GetLastError()));
            
if __name__ == '__main__':
    debugger = Debugger()
    debugger.load(b"C:\\WINDOWS\\System32\\calc.exe")
    cdll.msvcrt.system(b'pause');