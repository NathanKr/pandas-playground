import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)

print('\niterate on rows')
for index, row in df.iterrows():
    print(f'index : {index} , row[0] : {row[0]}')



