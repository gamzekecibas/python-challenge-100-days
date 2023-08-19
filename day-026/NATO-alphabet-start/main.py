import pandas as pd

'''
def spelling(alphabet_dict, word):
    spelled_word = [alphabet_dict[letter.upper()] for letter in word]
    return spelled_word
'''
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv', sep=',')
alphabet_dict = {alphabet_df.iloc[index, 0]:alphabet_df.iloc[index, 1] for (index, row) in alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Enter a word: ')
print([alphabet_dict[letter.upper()] for letter in user_word])