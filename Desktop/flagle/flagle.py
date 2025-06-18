import random
from PIL import Image

us_flag = Image.open("C:\\Users\\Eric\\Downloads\\us flag.png")
brazil_flag = Image.open("C:\\Users\\Eric\Downloads\\brazil flag.png")
SA_flag = Image.open("C:\\Users\\Eric\\Downloads\\SA flag.png")
canada_flag = Image.open("C:\\Users\\Eric\\Downloads\\canada flag.png")


flags = [
    (us_flag, "USA"),
    (brazil_flag, "Brazil"),
    (SA_flag, "SouthAfrica"),
    (canada_flag, "Canada")
]


(get_flag, get_country) = random.choice(flags) #tuple unpacking 
get_flag.show()


def start_game():
    lives = 6
    while lives > 0:
        guess = input("enter country name: ")
        if guess == get_country:
            print(f"you guessed correctly the country was {get_country} ")
            break
        elif guess != get_country:
            lives -= 1
            print(f"that is not correct you have {lives} guesses left")


        word_display = ""
        for i in range(len(get_country)):
            if guess[i] == get_country[i]:
                word_display += f"\033[92m{guess[i]}\033[00m"
            elif guess[i] in get_country:
                word_display += f"\033[93m{guess[i]}\033[00m"
            else:
                word_display += guess[i]

        print(word_display)



        if lives == 0 :
            print(f"you ran out of guesses the country was {get_country}")
            break



start_game()