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

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        alphabet_for_input_word = [var[w] for w in word]
    except KeyError:
        print("Sorry, enter letters from the alphabet only please.")
        generate_phonetic()
    else:
        print(alphabet_for_input_word)

generate_phonetic()