import pandas as pd

people = {
    "first": ["Nathan", 'Jane', 'John'], 
    "last": ["Krasney", 'Doe', 'Doe'], 
    "email": ["natankrasney@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)
print(f'df :\n{df}')
print(f'first row :\n{df.loc[0]}')
print(f"column first :\n{df['first']}")
