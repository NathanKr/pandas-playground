import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)

print('\niterate on rows')
for i_row, row in df.iterrows():
    print(f'row : {i_row}')
    for i_col in range(len(row)):
        print(f'row[{i_col}] : {row[i_col]}')



