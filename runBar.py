# -*- coding: UTF-8 -*-
import time
import sys
import progBar

progBar.actProBar(400)
progBar.PROGRESS_TOTAL=400
for x in range(400):
    progBar.proBar(x)
    time.sleep(0.05)
progBar.endProBar()
