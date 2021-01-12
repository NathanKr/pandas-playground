import pandas as pd
import numpy as np

d = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(d)
print("df1 : \n",df1)

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['aaa', 'bbb', 'ccc'])
print("df2 : \n",df2)
