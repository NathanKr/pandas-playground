import pandas as pd

people = {
    "first": ["Nathan", 'Jane', 'John'], 
    "last": ["Krasney", 'Doe', 'Doe'], 
    "email": ["natankrasney@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)

# default
print(f'--df :\n{df}')
print(f'--df.index : {df.index}') # default index
print(f'--df.columns : {df.columns}')

# change the index to email
df.set_index("email",inplace=True)
print(f'--changed df.index : {df.index}') 
print(f'--changed df :\n{df}')
print(f'--df.loc["natankrasney@gmail.com"] :\n{df.loc["natankrasney@gmail.com"]}')

