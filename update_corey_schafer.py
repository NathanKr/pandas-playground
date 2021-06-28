import pandas as pd

people = {
    "first": ["Nathan", 'Jane', 'John'], 
    "last": ["Krasney", 'Doe', 'Doe'], 
    "email": ["natankrasney@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


df = pd.DataFrame(people)
print(f'df , type(df) : {type(df)}\n{df}')

# update columns name
df.columns = ['first_name' , 'last_name' , 'email']
print(f'df after change columns name \n{df}')

# access by column name (provided there are no spaces)
print(f'df.first_name \n{df.first_name}')
