#!/usr/bin/python3

from ArgTools import ArgParser

class PlayfairEngine:

	bInitOK = False
	bInDebug = False

	def __init__(self, args):
		if (self.parseArgs(args)):
			self.bInitOK = True
		else: 
			print("Init failed in argument parser") 
			
	def showUsage(): 
		print("Usage: PlayFair {add params here}")


	def parseArgs(self, args): 

		subtestResults = []
		subtestResultMessages = []
		rval = True

		ap = ArgParser(args)

		self.bInDebug = ap.isInArgs("-debug", False)

		# TODO: Add arg parsing here.

		return(rval)


	def doAction(self):
		PlayfairEngine.showMsg("doAction not yet implemented.")


	def showMsg(msg):
		print(msg)


	def showDebugMsg(self, msg):
		if (self.bInDebug):
			print(msg)

		

