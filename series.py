import pandas as pd

labels = ['col1' , 'col2' , 'col3']
s1 = pd.Series(['a' , 'b' , 'c'] , index = labels)
print(f"s1\n{s1}")

s2 = pd.Series(['A' , 'B' , 'C'], index = labels)
print(f"s2\n{s2}")

df = pd.DataFrame([],columns=labels)
df = df.append(s1,ignore_index=True)
df = df.append(s2,ignore_index=True)

print(f"df\n{df}")
print(f"type(df['col1'].to_list()) : {type(df['col1'].to_list())}")
print(f"type(df['col1'].to_numpy()) : {type(df['col1'].to_numpy())}")