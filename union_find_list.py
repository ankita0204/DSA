"""
Created on Fri Aug  8 19:39:07 2020

@author: Ankita Dasgupta

Union Find Alorithm using Lists
"""

class uf:
    
    num=0
    ids=[]
        
    def __init__(self, inp):
        self.num=inp
        for i in range(inp):
            self.ids.append(i)
    
    # Prints the current id at each index
    def Print(self):
        print(self.ids)
    
    # Connects two elements by ovewriting the first element with the id of the second element
    def union(self, p, q):
        idp=self.ids[p]
        idq=self.ids[q]
        for i in range(self.num):
            if self.ids[i]==idp:
                self.ids[i]=idq
    
    # Checks if two elements have the same id
    def connected(self, p, q):
        return self.ids[p]==self.ids[q]
        
while True:
    try:
        num=int(input("Enter a number : "))
        break
    except:
        print("Invalid Input!")
        break
 
uf1=uf(num)
 
while True:
    inp=input('>')
    
    if inp.strip().upper().startswith('QUIT'):
            print("See you next time")
            quit()
            
    elif inp.strip().upper().startswith('UNION'):
        p=int(inp[(inp.find('(')+1):inp.find(',')])
        q=int(inp[(inp.find(',')+1):inp.find(')')])
        if (p in range(0,num)) and (q in range(0,num)):
            uf1.union(p,q)
        else:
            print('The numbers you entered are out of range')
            
    elif inp.strip().upper().startswith('CONNECTED'):
        p=int(inp[(inp.find('(')+1):inp.find(',')])
        q=int(inp[(inp.find(',')+1):inp.find(')')])
        if (p in range(0,num)) and (q in range(0,num)):
            if uf1.connected(p,q):
                print('CONNECTED!')
            else:
                print('NOT CONNECTED!')          
        else:
            print('The numbers you entered are out of range') 
                
    elif inp.strip().upper().startswith('PRINT'):
        uf1.Print()
        
    else:
        print(f'SyntaxError : {inp}')