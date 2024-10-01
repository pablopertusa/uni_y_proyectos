# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:57:24 2023

@author: pablo
"""

import pandas as pd

df = pd.read_csv('Crimes_2014.csv', delimiter=',')
print(df.iloc[5:10])
