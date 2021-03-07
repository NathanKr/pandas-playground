import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4], [4, 5, 6 , 7], [7, 8, 9 , 10]],
                   columns=['col1', 'col2', 'col3' , 'col4'])
print("df : \n",df)

print("\niterate col1")
for i in df.index: 
    print(df['col1'][i]) 

print("\niterate col1")
for item in df['col1']: 
    print(item) 

