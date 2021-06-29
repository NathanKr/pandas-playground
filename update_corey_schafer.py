import pandas as pd

people = {
    "first": ["Nathan", 'Jane', 'John'], 
    "last": ["Krasney", 'Doe', 'Doe'], 
    "email": ["natankrasney@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


def to_upper(item : str):
    return item.upper()

df = pd.DataFrame(people)
print(f'df , type(df) : {type(df)}\n{df}')

# update columns name
df.columns = ['first_name' , 'last_name' , 'email']
print(f'df after change columns name \n{df}')

# access by column name (provided there are no spaces)
print(f'df.first_name \n{df.first_name}')

# use apply to update series or datafram
df['first_name'] = df['first_name'].apply(to_upper)
print(f'df after apply to_upper to first_name column\n{df}')

# you can use also lambda function e.g. anonymouse function
df['last_name'] = df['last_name'].apply(lambda item :  item.lower())
print(f'df after apply lambda item.lower() to last_name column\n{df}')


# apply like this invoke len on every row
print(f'df.apply(len) : {df.apply(len)}')

df = df.applymap(len)
print ('df after df = df.applymap(len) : {df}')