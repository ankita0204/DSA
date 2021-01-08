"""
Created on Fri Aug  21 20:02:20 2020

@author: Ankita Dasgupta

Finding the minimum number of steps required to connect the top of a board to 
the bottom using the least amount of steps using the union find algorithm 
"""

import numpy as np
import random

# Union find algorithm using arrays 
class unionfind:
    size=0
    token=0
    
    def __init__(self, size):
        self.size= size
        self.token= np.empty(size, int)
        for i in range(size):
            self.token[i]=i
    
    # Function to print the entire board
    def Print(self):
        for i in range(self.size):
            print(self.token[i], end=' ')
        print('\n')
        
    # Checks if the tokens are matching
    def connected(self, p, q):
        return self.token[p]==self.token[q]
        
    # Assigns the same tokens to two keys 
    def union(self, p,q):
        tokp=self.token[p]
        tokq=self.token[q]
        for i in range(self.size):
            if self.token[i]==tokp:
                self.token[i]=tokq
                
class board:
    n=0
    size=0
    oc=0
    opened=0
    uf=0
    
    def __init__(self, bsize):
        self.n=bsize
        self.size=bsize*bsize
        self.oc=np.zeros(self.size+2, int)
        self.oc[0]=1
        self.oc[self.size+1]=1
        self.uf=unionfind(self.size+2)
        
    # Function to print the entire board
    def Print(self):
        for i in range(self.n): 
            print(self.oc[i*self.n+1:(i+1)*self.n+1])
            
    # Connects two elements of the board 
    def connect(self, p, q):
        if self.oc[p] and self.oc[q]:
            print('Connecting....', p, q)
            self.uf.union(p,q)

    # Checks if the top of the board and the bottom of the board are connected        
    def connected(self):
        return self.uf.connected(0,self.size+1)
    
    # Opens random elements of the board    
    def open(self, i):
        if self.oc[i]:
            return
        self.opened+=1
        print('Random Number Position: ',i)
        self.oc[i]=1
        if i==1:
            print('Top Left')
            self.connect(i, 0)
            self.connect(i, i+1)
            self.connect(i, i+self.n)
        elif i==self.n:
            print('Top Right')
            self.connect(i, i-1)
            self.connect(i, i+self.n)
            self.connect(i, 0)
        elif i==self.size:
            print('Bottom Right ')
            self.connect(i, self.size+1)
            self.connect(i, i-1)
            self.connect(i, i-self.n)
        elif i==(self.size-self.n)+1:
            print('Bottom Left')
            self.connect(i, self.size+1)
            self.connect(i, i+1)
            self.connect(i, i-self.n)
        elif i>1 and i<self.n:
            print('Top Row')
            self.connect(i, 0)
            self.connect(i, i+self.n)
            self.connect(i, i+1)
            self.connect(i, i-1)
        elif i>(self.size-self.n) and i<self.size:
            print('Bottom Row')
            self.connect(i, self.size+1)
            self.connect(i, i+1)
            self.connect(i, i-1)
            self.connect(i, i-self.n)
        elif (i%self.n)==1:
            print('Left Collumn')
            self.connect(i, i+1)
            self.connect(i, i+self.n)
            self.connect(i, i-self.n)
        elif (i%self.n)==0:
            print('Right Collumn')
            self.connect(i, i-1)
            self.connect(i, i-self.n)
            self.connect(i, i+self.n)
        else:
            print('Middle')
            self.connect(i, i+1)
            self.connect(i, i-1)
            self.connect(i, i-self.n)
            self.connect(i, i+self.n)
        self.Print()    
        
inp=int(input('Enter board size: '))
b1=board(inp)
while True:     
    n=random.randrange(1, (inp*inp)+1)
    b1.open(n)
    if b1.connected():
        print('\n\nCONNECTED!!!')
        print('Number of Squares opened: ',b1.opened)
        break
    else:
        continue