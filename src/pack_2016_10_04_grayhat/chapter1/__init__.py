from ctypes import *

cdll.msvcrt.printf(b'testing:%s',b"hello");