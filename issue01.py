# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 16:10:26 2018

@author: WITHJS
"""

import pandas as pd
df = pd.DataFrame({'sales': [3, 2, 3],'visits': [20, 42, 28], 'day': ['Monday', 'Tuesday', 'Wednesday']})

ax = df.plot.area(x='day')
ax