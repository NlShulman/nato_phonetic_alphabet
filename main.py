import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {nato_alpha.letter: nato_alpha.code for (index, nato_alpha) in nato_alpha.iterrows()}

user_word = input("Enter a word: ").upper()

natto_letters = [nato_dict[letter] for letter in user_word]
print(natto_letters)




