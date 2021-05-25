import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])

all_rows_via_iloc = df.iloc[:,:]
print(f'type(all_rows_via_iloc) : {type(all_rows_via_iloc)}')
print(f'all_rows_via_iloc : \n{all_rows_via_iloc}')

first_row_via_iloc = df.iloc[0,:]
print(f'type(first_row_via_iloc) : {type(first_row_via_iloc)}')
print(f'first_row_via_iloc : \n{first_row_via_iloc}')

first_col_via_iloc = df.iloc[:,0]
print(f'type(first_col_via_iloc) : {type(first_col_via_iloc)}')
print(f'first_col_via_iloc : \n{first_col_via_iloc}')

