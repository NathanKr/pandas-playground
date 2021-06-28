import pandas as pd
dict = {'col1' : ['1' , '1.2' , 'a' , '123' , ''] , 
        'col2' : [1 , 1.2 , 11 , 123 , -1]    }

df = pd.DataFrame(dict)

print(f'df.isna : {df.isna()}')
print(f'type(df.iloc[:,0]) : {type(df.iloc[:,0])}')
print(f'type(df.iloc[:,1]) : {type(df.iloc[:,1])}')
print(df.iloc[:,0].str.isnumeric())