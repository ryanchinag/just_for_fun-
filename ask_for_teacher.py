'''
import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, name in itertools.groupby(names, first_letter):
    print(letter, list(names))
    '''
#照理來說是可以排序為何沒有排到??
'''
import numpy as np
import matplotlib.pyplot as plt 
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
'''
#跑出結果與書本不同 是否正常??
'''
import pandas as pd
pd.Series(dtype='float64')
Type_new = pd.Series([],dtype=pd.StringDtype()) 
chunker = pd.read_csv('C:/Users/ryans/Desktop/DATA/ex6.csv', chunksize=1000)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value = 0)

tot = tot.sort_values(ascending=False)'''

#The default dtype for empty Series will be 'object' instead of 'float64' in a future version. Specify a dtype explicitly to silence this warning.
#tot = pd.Series([])
#上網也看不到相關資料