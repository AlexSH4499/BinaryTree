import sys
import os

class Stack:

	def __init__(self):
		self.li = []

	def isEmpty(self):
		return self.li == []
		
	def pop(self):
		return self.li.pop()
		
	def push(self,item):
		self.li.append(item)
		
	def peek(self):
		return self.li[len(self.li)-1]
		
	def size(self):
		return len(self.li)