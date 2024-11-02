#!/usr/bin/env python3

'''
## Exceptions
'''
class CellIndexError(Exception):
	pass


'''
## Class for the basic cell
'''
class cell:
	
	## Class variables
	# Board size, number of states (-1 is a void, and 0 is a valid state)
	xSize = 1
	ySize = 1
	nStts = 1
	
	# Class initialize
	def setBoard(inXSize = 1, inYSize = 1):
		cell.xSize = max(1,inXSize)
		cell.ySize = max(1,inYSize)
		print("Board set to {} x {}".format(cell.xSize, cell.ySize))
	
	# Constructor
	def __init__(self, inIndex, inToggle = -1):
		
		# self.index  = indicates position in the board
		self.index = inIndex
		self.state = -1
		
		# Set all possible neighbors, default to none for edge cells
		if self.isEdge():
			self.state = -1
			self.neighX, self.neighY = [], []
		else:
			self.state = inToggle
			self.neighX, self.neighY = [inIndex-1, inIndex+1], [inIndex - (cell.xSize+2), inIndex + (cell.xSize+2)]
		
		# All neighbors
		self.neighA = self.neighX + self.neighY
	
	
	# Row / column
	def getRow(self):
		return self.index // (cell.xSize+2)
	
	def getCol(self):
		return self.index %  (cell.xSize+2)
	
	## Edge finder
	def isEdge(self):
		if   self.index < 0 or self.index >= (cell.xSize+2)*(cell.ySize+2):
			raise CellIndexError
		elif self.getRow() == 0 or self.getRow() == cell.ySize + 1:
			return True
		elif self.getCol() == 0 or self.getCol() == cell.xSize + 1:
			return True
		else:
			return False

'''
## Class for the basic board
'''
class board:
	pass
