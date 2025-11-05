import random
import time

def draw_card(hand):
    """add a new card to the hand randomly"""
    card = random.choice(list(cards_dic.keys()))
    hand.append(card)

def hand_value_check(hand):
    """Evaluate the point total of the hand, including ace weirdness"""
    total = 0
    for card in hand:
        total += cards_dic[card]
    #reduce Ace 11s to 1s to try not to bust
    num_aces = hand.count("Ace")
    while total > 21 and num_aces > 0:
        total -= 10
        num_aces -= 1
    return total


cards_dic = {"Ace" : 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}
user_hand = []
house_hand = []

#draw starting cards
draw_card(user_hand)
draw_card(user_hand)
draw_card(house_hand)
draw_card(house_hand)
user_total = hand_value_check(user_hand)
house_total = hand_value_check(house_hand)
print(f"You have:\t{user_hand}\nHouse has:\t{house_hand[0]} [?]")
#print(f"\nThat means you have {user_total} points, and the house has {house_total} points, dummy.")

#ask the user if they want a hit
hit_bool = False
hit_input = input("Hit or Stay? (H/S):\t").upper()
while (hit_input != "H") and (hit_input != "S"):
    hit_input = input("What did you say??? Hit or Stay! (H/S):\t").upper()
if hit_input == "H": hit_bool = True

#hit and assess for the user as many times as they'd like until they bust
while hit_bool:
    draw_card(user_hand)
    print(f"You have:\t{user_hand}\nHouse has:\t{house_hand[0]} [?]")
    user_total = hand_value_check(user_hand)
    if user_total > 21:
        print(f"{user_total} points! You LOSE!!")
        exit()
    if user_total == 21:
        print(f"{user_total} points! BLACKJACK!!! :D")
        time.sleep(3)
        break

    hit_bool = False
    hit_input = input("Hit or Stay? (H/S):\t").upper()
    while (hit_input != "H") and (hit_input != "S"):
        hit_input = input("What did you say??? Hit or Stay! (H/S):\t").upper()
    if hit_input == "H": hit_bool = True

#time for the house to play!
print(f"You have:\t{user_hand}\nHouse has:\t{house_hand}")
while user_total > house_total and house_total < 22:
    time.sleep(3)
    draw_card(house_hand)
    print(f"You have:\t{user_hand}\nHouse has:\t{house_hand}")
    house_total = hand_value_check(house_hand)
    if house_total > 21:
        print(f"{house_total} points; House BUSTS, you Win!!!")
        exit()
    if house_total == 21:
        print("House BLACKJACK, oh no!!!")
        exit()
if user_total == house_total:
    print(f"{user_total} to {house_total}, tie game; PUSH")
    exit()
print(f"{user_total} to {house_total}, house wins :(")