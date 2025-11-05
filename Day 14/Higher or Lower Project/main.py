import random
import time

import art

#accounts to choose from
insta_dic = {    "instagram\tSocial media platform"  : 694,
                "Cristiano Ronaldo\tFootballer"     : 666,
                "Lionel Messi\tFootballer"          : 506,
                "Selena Gomez\tMusician and actress": 417,
                "Kylie Jenner\tMedia personality"   : 392,
                "Dwayne Johnson\tActor/Wrestler"    : 392,
                "Ariana Grande\tMusician/actress"   : 374,
                "Kim Kardashian\tMedia witch"       : 355,
                "Beyonce\tBEYONCE"                  : 309,
                "Nike\tSportswear"                  : 299,
                "Taylor Swift\tMusician"            : 282,
                "National Geographic\tMagazine"     : 277,
                "Zendaya\tActress and singer"       : 177,
                "Kevin Hart\tComedian and actor"    : 176,
                "Billie Eilish\tMusician"           : 124,
                "NASA\tSpace agency"                : 96.8,
                "NBA\tProfessional basketball"      : 90.8,
}

#the game
def the_game():
    score = 0
    lose_bool = False
    while not lose_bool:
        print("\n" * 100)
        print(art.logo)
        choice1 = random.choice(list(insta_dic.keys()))
        choice2 = random.choice(list(insta_dic.keys()))
        while choice1 == choice2:
            choice2 = random.choice(list(insta_dic.keys()))
        print(choice1)
        print(art.vs)
        print(choice2)

        user_choice = input("Who has more followers? 1 or 2:\t")
        if ((insta_dic[choice1] > insta_dic[choice2]) and (user_choice == "1")) or ((insta_dic[choice1] < insta_dic[choice2]) and (user_choice == "2")):
            score += 1
            print(f"Correct! {choice1}:\t{insta_dic[choice1]}MIL vs {choice2}:\t{insta_dic[choice2]}MIL")
        else:
            print(f"Incorrect! {choice1}:\t{insta_dic[choice1]}MIL vs {choice2}:\t{insta_dic[choice2]}MIL")
            lose_bool = True
        time.sleep(3)

    print(f"\n\nYou scored {score} points!")
    return score

#loop
keep_playing_bool = True
max_score = 0
while keep_playing_bool:
    score = the_game()
    if score > max_score:
        max_score = score
        print("That's a new high score!!")
    user_input = input("Would you like to play again? (Y/n):\t").lower()
    if user_input == 'n':
        keep_playing_bool = False

print(f"\n\nYour high-score was {max_score}. Well done!")