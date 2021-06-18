import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)

for col_name in df:
    print(f'col_name : {col_name}')
    col = df[col_name]
    print(f'col\n{col}')
    print(f'col[0] : {col[0]}')


