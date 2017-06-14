import os
import sys


class Memoize:
    def __init__(self,fn):
        self.fn = fn #function binded to class
        self.memo = {} #Dictionary to be used as memory for functions
                        # Acts as a hashmap of sorts
    #defines each function call
    #binds them by argument to the dictionary
    def __call__(self, fn, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
            return self.memo[arg]

@Memoize
def function():
    #do something here
    return function()
