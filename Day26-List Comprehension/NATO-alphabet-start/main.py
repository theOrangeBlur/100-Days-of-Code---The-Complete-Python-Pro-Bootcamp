import pandas

#TODO 1. Create a dictionary in this format: {A: Alpha}
data = pandas.read_csv("Day26-List Comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Give me a word:\t")
nato_list = [dict[letter.title()] for letter in user_word]
print(nato_list)
