#! /usr/bin/env python
'''
Copyright (C) 2012  Diego Torres Milano
Created on Apr 30, 2013

@author: diego
'''


import sys
import os
import time
# PyDev sets PYTHONPATH, use it
try:
    for p in os.environ['PYTHONPATH'].split(':'):
        if not p in sys.path:
            sys.path.append(p)
except:
    pass

try:
    sys.path.append(os.path.join(os.environ['ANDROID_VIEW_CLIENT_HOME'], 'src'))
except:
    pass
from com.dtmilano.android.adb import adbclient	
# from com.android.monkeyrunner.easy import EasyMonkeyDevice

from com.dtmilano.android.viewclient import ViewClient

# ViewClient(*ViewClient.connectToDeviceOrExit(verbose=True)).traverse(transform=ViewClient.TRAVERSE_CIT)
device, serialno = ViewClient.connectToDeviceOrExit()

device.drag((960,1497),(214,1496),0)
device.drag((214,1496),(500,20),0)


# device.touch(610, 1734, adbclient.DOWN_AND_UP)

# device.dragDip((301.33, 140.67), (143.33, 400.67), 20, 20, 0)