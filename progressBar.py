# -*- coding: UTF-8 -*-
import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
parts = ['','▏','▎','▍','▌','▋','▊','▉']

print
for x in range(400):
    print(CURSOR_UP_ONE + ERASE_LINE)
    print('Loading'+('.'*int((x/2)%5))+(' '*int(5-(x/2)%5))+' |'+('█'*int(x/8))+parts[x%8]+(' '*int((400-x)/8))+'| Loading'+('.'*int((x/2)%5))+(' '*int(5-(x/2)%5)),end="")
    sys.stdout.flush()
    time.sleep(0.05)
print(CURSOR_UP_ONE + ERASE_LINE)
print('Done Loading'+' |'+('█'*(400/8))+'| Done Loading',end="")
print()
