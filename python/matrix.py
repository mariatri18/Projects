import numpy as np
from os import system, name

def clear(): 
    if name == 's': 
        _ = system('cls') 
clear()

s = 62
i=0
with open('python/outfile.txt', 'w') as out:
    for i in range (0, s):
            print(i+1) 
            A = np.random.randint (2, size=(8,8))
            print(A,"\n")
            out.write(str(A))
            out.write(str("\n\n"))
            