import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_codes = {row.letter: row.code for (index, row) in data_frame.iterrows()}

ask_for_input = True
while ask_for_input:
    try:
        user_word = input("What word do you want to spell? ")
        coded_output = [alphabet_codes[letter.upper()] for letter in user_word]
        print(coded_output)
    except KeyError:
        print("Only alphabet letters are accepted. Please try again.")
    else:
        ask_for_input = False

