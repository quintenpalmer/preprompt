#!/usr/bin/env python

import os
import time
import sys
from datetime import datetime

def reset_file(filename):
	t = time.mktime(datetime.now().timetuple())-86400
	os.utime(filename,(t,t))

if len(sys.argv) > 1:
	reset_file(sys.argv[1])
else:
	print 'must provide file'
