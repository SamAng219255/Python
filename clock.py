# -*- coding: UTF-8 -*-
import time
import sys

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

if len(sys.argv)<2:
 length=1
else:
 length=int(sys.argv[1])
print()
for i in range(length):
 year=int(time.time()/(60*60*24*365.24)+1970)
 year=str(year)
 day=int(time.time()/(60*60*24))-365.24*int(time.time()/(60*60*24*365.24))
 day=("0"*(3-len(str(int(day)))))+str(int(day))
 hour=int(time.time()/(60*60))-24*int(time.time()/(60*60*24))
 hour=("0"*(2-len(str(hour))))+str(hour)
 minute=int(time.time()/(60))-60*int(time.time()/(60*60))
 minute=("0"*(2-len(str(minute))))+str(minute)
 second=int(time.time())-60*int(time.time()/(60))
 second=("0"*(2-len(str(second))))+str(second)
 print(CURSOR_UP_ONE+CURSOR_UP_ONE+ERASE_LINE)
 print(year,day,hour,minute,second,sep=":")
 time.sleep(1)
print()
