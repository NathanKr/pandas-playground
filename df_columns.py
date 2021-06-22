import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]])
print("df : \n",df)

print(f'df.columns before : {df.columns}')

# remove second column
df.drop([1], axis=1,inplace=True)
print(f'df.columns before : {df.columns}')
print("df : \n",df)

