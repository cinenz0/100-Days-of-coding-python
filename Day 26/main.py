import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pd.read_csv('nato_phonetic_alphabet.csv')

new_dict = {value['letter']:value['code'] for (index, value) in df.iterrows() }
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input('wrd: ').upper()

user_list = [new_dict[letter] for letter in user ]
print(user_list)
