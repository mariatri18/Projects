import numpy as np
from os import system, name
import pandas as pd
import csv

s = 2

with open('python/outfile.csv','w') as out:
    #out_reader = csv.writer(out)
    
    for l in range (0, s):
            
            a = np.random.randint (2, size=(8,8))
            alist = list(a)
            print(a,"\n")
            print(alist)
            
               
            df = pd.DataFrame([alist[0]]+[alist[1]]+[alist[2]]+[alist[3]]+[alist[4]]+[alist[5]]+[alist[6]]+[alist[7]])

            df.to_csv("python/outfile.csv", line_terminator='\n', mode='a')