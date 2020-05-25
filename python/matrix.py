import numpy as np
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
clear()

s = 5
i=0

for i in range (0, s):
    print(i+1) 
    A = np.random.randint (2, size=(8,8))
    print(A,"\n")