# -*- coding: UTF-8 -*-
import time
import sys

PROGRESS_TOTAL = 1
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
parts = ['','▏','▎','▍','▌','▋','▊','▉']
def actProBar(total):
    PROGRESS_TOTAL = total
    print
def proBar(progress):
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    print '|'+('█'*((400*progress/PROGRESS_TOTAL)/8))+parts[(400*progress/PROGRESS_TOTAL)%8]+(' '*((400-(400*progress/PROGRESS_TOTAL))/8))+'|'
    sys.stdout.flush()
def endProBar():
    print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    print '|'+('█'*50)+'|'
