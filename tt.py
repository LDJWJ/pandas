import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({'sales': [3, 2, 3],
             'visits': [20, 42, 28],
            'day': ['Monday', 'Tuesday', 'Wednesday']})

ax = df.plot.area(x='day')
ax