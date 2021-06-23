import pandas as pd

people = {
    "first": ["Nathan", 'Jane', 'John'], 
    "last": ["Krasney", 'Doe', 'Doe'], 
    "email": ["natankrasney@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)
print(f'\ndf :\n{df}')
print(f'\ndf.index : {df.index}')
print(f'\nfirst row using df.loc[0] :\n{df.loc[0]}')
print(f'\nsecond row using df.loc[1] :\n{df.loc[1]}')
print(f"\ncolumn first using df['first'] :\n{df['first']}")

df.drop([1],inplace=True)
print(f'\ndf after drop second row:\n{df}')
print(f'\ndf.index after drop second row: {df.index}')
# print(f'\ndf.loc[1] :\n{df.loc[1]}') -->this will throw because the index does not exist !!

# reset index will help
df.reset_index(inplace=True)
print(f'\ndf.index after drop second row: {df.index}')
print(f'\ndf.loc[1] :\n{df.loc[1]}') # now it will work
