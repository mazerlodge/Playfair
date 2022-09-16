#!/usr/bin/python3

import sys
from PlayfairEngine import PlayfairEngine 

pe = PlayfairEngine(sys.argv) 

if (not pe.bInitOK):
	PlayfairEngine.showUsage()
else:
	pe.doAction()

