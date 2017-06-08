import os
import io
import sys
'''
	File IO
'''
def open_file(file,buffering=0):
	f = open(file,"rw",buffering)
    return f
	
def write_file(str,index = 0, file):
	if(index < 0)
		print("Invalid index!")
		return
	#otherwise
	file.seek(index)
	file.write(str)
	return

class BinaryTree():
	def __init__(self,rootid):
		self.left = None
		self.right = None
		self.rootid = rootid
	
	def getLeftChild(self):
		return self.left
	
	def getRightChild(self):
		return self.right
		
	def setNodeValue(self,val):
		self.rootid = val
	
	def getNodeValue(self):
		return self.rootid
		
	def addRightChild(self, child):
		self.right = child
		return
	
	def addLeftChild)(self, child):
		self.left = child
		return
	