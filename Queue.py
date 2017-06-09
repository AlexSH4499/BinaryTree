import os 
import sys
from collections import deque

class Queue:

	def __init__(self):
		self.d = deque()
		
	def isEmpty(self):
		return self.d == []
		
	def push(self, item):
		self.d.append(item)
		
	def pop(self):
		return self.d.popleft()