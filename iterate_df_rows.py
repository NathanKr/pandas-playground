import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)

print('\niterate on rows')
for i, row in df.iterrows():
    print(f'i : {i} , row[0] : {row[0]}')



