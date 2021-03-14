import pandas as pd
df = pd.DataFrame([[1, 2, 3, 4], [4, None, 2, 1], [4, 5, -6 , 7], [7, 8, -9 , 10], [11, 23, 13, 14]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df\n",df)
print('df.isnull().any()\n',df.isnull().any())
print('df.mean()\n',df.mean())
df.dropna(inplace=True)
print('df after remove rows with missing values',df)