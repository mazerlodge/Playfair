#!/usr/bin/python3

from ArgTools import ArgParser


class PlayfairEngine:

	bInitOK = False
	bInDebug = False
	key = "NOT_SET"
	encPhrase = "NOT_SET" 
	plainPhrase = "NOT_SET"

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
			self.key = ap.getArgValue("-key")
			rval = True
			subtestResultMessages.append("-key %s" % self.key)
		else:
			subtestResultMessages.append("-key param not found")
		subtestResults.append(rval)

		# check for -enctext param
		bHasEncText = False
		if (ap.isInArgs("-enctext", True)):
			encPhrase = ap.getArgValue("-enctext")
			bHasEncText = True
			subtestResultMessages.append("-enctext %s" % encPhrase)
		else:
			subtestResultMessages.append("-enctext param not found")

		# check for -plaintext param
		bHasPlainText = False
		if (ap.isInArgs("-plaintext", True)):
			plainPhrase = ap.getArgValue("-plaintext")
			bHasPlainText = True
			subtestResultMessages.append("-plaintext %s" % plainPhrase)
		else:
			subtestResultMessages.append("-plaintext param not found")
		
		# Determine if all subtests passed
		for aMsg in subtestResultMessages:
			if (self.bInDebug):
				msg = "Arg subtest {0}".format(aMsg)
				print(msg)

		# Test for [-plaintext | -enctext] (one of these is required)
		bRval = False
		if (bHasEncText or bHasPlainText):
			subtestResultMessages.append("Either encText or plainText was found")
			subtestResults.append(True)
		else: 
			subtestResultMessages.append("Either encText or plainText was *not* found")
			subtestResults.append(False)

		if (self.bInDebug):
			for aMsg in subtestResultMessages:
				self.showDebugMsg(aMsg)

		for aSubResult in subtestResults:
			rval = rval and aSubResult

		return(rval)


	def doAction(self):
		PlayfairEngine.showMsg("doAction not yet implemented.")
		
		# TODO: Collapse -key (e.g. Tomorrow = TOMRW)
		PlayfairEngine.showMsg(self.bInDebug)
		self.showDebugMsg("Currently have key = %s" % self.key)

	def showMsg(msg):
		print(msg)


	def showDebugMsg(self, msg):
		if (self.bInDebug):
			print(msg)

		

