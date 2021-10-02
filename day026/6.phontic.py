import os
import pandas
root = os.path.dirname(os.path.abspath(__file__)) + "/"

data = pandas.read_csv(f"{root}nato_phonetic_alphabet.csv")

alphabet = {row.letter:row.code for (index,row) in data.iterrows()}
user_input = input("Ebter a word: ").strip()

new_user_input = [alphabet[key.upper()] for key in user_input if alphabet.__contains__(key.upper())]
print(new_user_input)