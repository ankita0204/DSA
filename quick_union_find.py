"""
Created on Fri   14 19:57:36 2020

@author: Ankita Dasgupta

Quick Union Find Method using Arrays 
"""

import numpy as np

class UF:
    
    num=0
    ids=[]
    size=0
        
    def __init__(self, inp):
        self.num=inp
        self.ids=np.empty(inp,int)
        self.size=np.ones(inp,int)
        
        for i in range(inp):
            self.ids[i]=i
    
    # Used to check the connection faster
    def root(self,p):        
        while p!= self.ids[p]:
            self.ids[p]=self.ids[self.ids[p]] # for path compression
            p=self.ids[p]
        return p
        
    def Print(self):
        print(self.ids)
    
    # Weighted Tree Union Method
    def union(self, p, q):          
        i=self.root(p)
        j=self.root(q)
        if i==j: return
        if self.size[i]<self.size[q]:         # i tree is smaller than j tree
            self.ids[i]=j
            self.size[j]=self.size[i]
        else:
            self.ids[j]=i
            self.size[j]=self.size[j]
        
    def connected(self, p, q):
        return self.root[p]==self.root[q]

