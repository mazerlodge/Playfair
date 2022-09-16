#!/usr/bin/python3

from ArgTools import ArgParser

class PlayfairEngine:

	bInitOK = False
	bInDebug = False
	key = "NOT_SET"

	def __init__(self, args):
		if (self.parseArgs(args)):
			self.bInitOK = True
		else: 
			print("Init failed in argument parser") 
			
	def showUsage(): 
		print("Usage: PlayFair -key required [-plaintext | -enctext]")


	def parseArgs(self, args): 

		subtestResults = []
		subtestResultMessages = []
		rval = True

		ap = ArgParser(args)

		self.bInDebug = ap.isInArgs("-debug", False)

		# check for -key param
		rval = False
		if (ap.isInArgs("-key", True)):
			key = ap.getArgValue("-key")
			rval = True
		subtestResults.append(False)
		subtestResultMessages.append("-key %s" % key)
		
		# Determine if all subtests passed
		for aMsg in subtestResultMessages:
			if (self.bInDebug):
				msg = "Arg subtest {0}".format(aMsg)
				print(msg)

		for aSubResult in subtestResults:
			rval = rval and aSubResult

		return(rval)


	def doAction(self):
		PlayfairEngine.showMsg("doAction not yet implemented.")


	def showMsg(msg):
		print(msg)


	def showDebugMsg(self, msg):
		if (self.bInDebug):
			print(msg)

		

