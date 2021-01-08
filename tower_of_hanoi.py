"""
Created on Fri Jan  8 23:20:02 2021

@author: Ankita Dasgupta

Tower of Hanoi
"""

# Recurssive Function
def TowerOfHanoi(n, start, end, middle):
	if n ==1:
		print("Move", n, "from tower", start, "to", end)
	else:
		TowerOfHanoi(n-1, start, middle, end)
		print("Move",n,"from tower",start,"to",end)
		TowerOfHanoi(n-1, middle, end, start)

print("> Enter the number of loops")
n = int(input("> "))
TowerOfHanoi(n, "A", "C", "B")