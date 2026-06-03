import pandas as pd
import os

#Nato alphabet
file_path = os.path.join("utils", "nato_phonetic_alphabet.csv")
current_dir = os.getcwd()
alphabet_full_path = os.path.join(current_dir, file_path)

#Loop through CSV using pandas
data = pd.read_csv(alphabet_full_path)

var ={ row.letter:row.code for (index, row) in data.iterrows()}
print(var)

#TODO 1. Create dictionary in format:
#{"A":"Alfa", "B":"Bravo", etc}

#TODO 2. Input word and spell it
word = input("Enter a word: ").upper()
alphabet_for_input_word = [var[w] for w in word]
print(alphabet_for_input_word)