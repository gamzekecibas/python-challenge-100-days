import pandas as pd

'''
def spelling(alphabet_dict, word):
    spelled_word = [alphabet_dict[letter.upper()] for letter in word]
    return spelled_word
'''
alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv', sep=',')
alphabet_dict = {alphabet_df.iloc[index, 0]:alphabet_df.iloc[index, 1] for (index, row) in alphabet_df.iterrows()}

def generate_phonetic():
    user_word = input('Enter a word: ')
    try:
        nato_letters = [alphabet_dict[letter.upper()] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(nato_letters)

generate_phonetic()