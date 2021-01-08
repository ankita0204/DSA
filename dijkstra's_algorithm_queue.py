"""
Created on Fri Sep  11 23:10:36 2021

@author: Ankita Dasgupta

Dijkstra's Algorithm application with the help of Queue
"""

import numpy as np

class queue:
    size = None
    tail = None         # End of the Queue: Elements enter from here
    head = None         # Front of the Queue: Elements are deleted from here
    type = None
    arr = None
    
    def __init__(self, arrtype):
        self.arrtype = arrtype
        self.size = 1
        self.arr = np.zeros(self.size,arrtype)
        self.tail = 0
        self.head = 0
        
    def empty(self):
        return self.head == self.tail 
    
    def dequeue(self):
        if self.empty():
            print(' Queue Underflow')
            return 
        a = self.arr[self.head]
        self.head = self.head + 1
        return a
        
    def full(self):
        return self.tail == self.size
        
    def enqueue(self, a):
        if self.full():
            temp = self.arr
            self.size *= 2
            self.arr = np.zeros(self.size, self.arrtype)
            for i in range(len(temp)):
                self.arr[i]=temp[i]
        self.arr[self.tail] = a
        self.tail += 1
        
# Dijstras Algorithm 
valstack = queue(int)
opstack = queue(np.chararray)

inp = input(' > ' )
token=inp.split()

for tok in token:
    if tok== '(':
        pass
        
    elif tok== ')':
        r = valstack.dequeue()
        l = valstack.dequeue()
        op=opstack.dequeue()
        if op == '+':
            valstack.enqueue(l+r)
        elif op == '-':
            valstack.enqueue(l-r)
        elif op == '*':
            valstack.enqueue(l*r)
        elif op == '/':
            valstack.enqueue(l/r)
        elif op == '^':
            valstack.enqueue(l**r)
        else:
            print("ERROR: INVALID OPERATOR")
            
    elif '0' <= tok <= '999':
        valstack.enqueue(int(tok))      
            
    elif tok in ['+','-','*','/','^']:
        opstack.enqueue(tok)
        
    elif tok == '=':
        print('Result : ', valstack.dequeue())
        assert valstack.empty() == True and opstack.empty() == True
    
print(opstack.empty())
print(valstack.empty())