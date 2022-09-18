#!/usr/bin/python3

from ArgTools import ArgParser


class PlayfairEngine:

	bInitOK = False
	bInDebug = False
	key = "NOT_SET"

	def __init__(self, args):
		self.bInitOK = self.parseArgs(args)	
		if (not self.bInitOK):
			self.showDebugMsg("PlayfairEngine __Init__ failed in argument parser") 
			
			
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
			subtestResultMessages.append("-key %s" % key)
		else:
			subtestResultMessages.append("-key param not found")
		subtestResults.append(rval)
		
		# Determine if all subtests passed
		for aMsg in subtestResultMessages:
			if (self.bInDebug):
				msg = "Arg subtest {0}".format(aMsg)
				print(msg)

		# TODO: add test for [-plaintext | -enctext] (one of these is required)
		
		if (self.bInDebug):
			for aMsg in subtestResultMessages:
				self.showDebugMsg(aMsg)

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

		

