import numpy as np
from os import system, name
import pandas as pd

def clear(): 
    if name == 's': 
        _ = system('cls') 
clear()

s = 2
l = 0
xl = 0

with open('python/outfile.csv', 'w' ) as out:
    
    for l in range (0, s):
            
            print(l+1) 
            a = np.random.randint (2, size=(8,8))
            print(a,"\n")
            
            for row in a[s]: 
                for l in range(0, s):
                
                    df = pd.DataFrame({'x1': [a[0]],'x2': [a[1]],'x3': [a[2]],'x4': [a[3]],'x5': [a[4]],'x6': [a[5]],'x7': [a[6]],'x8': [a[7]]})
                    df.to_csv('python/outfile.csv')
                # out.write(str(a))
                # out.write(str("\n\n"))
