"""
Created on Fri Sep  11 23:15:03 2021

@author: Ankita Dasgupta

Dijkstra's Algorithm application with the help of Stacks
"""

# Class for Stacks using Arrays 

import numpy as np

class stack:
    size = None
    last = None
    typ = None
    arr = None
    
    def __init__(self, typ):
        self.size = 1
        self.last = 0
        self.typ = typ
        self.arr = np.zeros(self.size, self.typ)
        
    def full(self):
        return self.last == self.size
    
    def empty(self):
        return not self.last
    
    def push(self, num):
        if self.full():
            var = self.arr
            self.size = self.size*2
            self.arr = np.zeros(self.size, self.typ)
            for i in range(len(var)):
                self.arr[i] = var[i]
        self.arr[self.last] = num
        self.last = self.last + 1
        
    def pop(self):
        if self.empty():
            print('ERROR : EMPTY STACK')
            return
        self.last = self.last - 1
        val = self.arr[self.last]
        return val      


# Dijstras Algorithm
    
valstack = stack(int)
opstack = stack(np.chararray)

inp = input(' > ' )
token=inp.split()

for tok in token:
    if tok== '(':
        pass
        
    elif tok== ')':
        r = valstack.pop()
        l = valstack.pop()
        op=opstack.pop()
        if op == '+':
            valstack.push(l+r)
        elif op == '-':
            valstack.push(l-r)
        elif op == '*':
            valstack.push(l*r)
        elif op == '/':
            valstack.push(l/r)
        elif op == '^':
            valstack.push(l**r)
        else:
            print("ERROR: INVALID OPERATOR")
            
    elif '0' <= tok <= '999':
        valstack.push(int(tok))      
            
    elif tok in ['+','-','*','/','^']:
        opstack.push(tok)
        
    elif tok == '=':
        print('Result : ', valstack.pop())
        assert valstack.empty() == True and opstack.empty() == True
        
