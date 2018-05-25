'''
Created on Oct 3, 2017

@author: Sam_I_Am
'''

import numpy as np
import pandas as pd
import sys

print(sys.path)

class SRFtestclass:
    def __init__(self, input_array):
        
        print('This class has initialized')
        
        try:
            np.nditer(input_array)
            pass
        except:
            ValueError
            print('The input array was not a true, iterable array')
        finally:
            print("this block is always executed")
        

test_array = np.linspace(0, 100, 15)
test_not_array = pd.Series([60,50,20,30])
print(type(test_not_array))
for i in np.nditer(test_not_array): print(i)
