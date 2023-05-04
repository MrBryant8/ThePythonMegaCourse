import json
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    if word in data:       
        result = data[word]
        for n in range(0,len(result)):
            print(result[n])
        return "\n"
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) != 0:
        while True:
            user_answer = input(f"Did u mean {get_close_matches(word,data.keys(),cutoff=0.8)[0]}?\
            \nType Y for yes or N for no:")
            if user_answer == 'Y':
                word = get_close_matches(word, data.keys(), cutoff=0.8)[0]
                for n in range(0, len(data[word])):
                    print(data[word][n])
                return "\n"
            elif user_answer == 'N':
                return "Our system cannot recognise this word.Please double check it"
            else:
                print("Only Y or N allowed.Try again\n")

    else:
        return "The entered word is not inside our database.Please double check it"


data = json.load(open("data.json", "r"))
user_input = input("Enter a word:")
print(translate(user_input))
