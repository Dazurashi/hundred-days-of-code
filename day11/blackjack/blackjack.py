#TODO Not ready, just busy today so couldn't finish it
from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
player_cards = []

def deal_card(hand):
    hand.append(random.choice(cards))
    return hand

def play_game(player, computer):
    player = deal_card(player)
    player = deal_card(player)
    computer = deal_card(computer)
    computer = deal_card(computer)
    return player, computer

def check_sum(player, computer):
    if sum(player) == 21:
        print("You win")
    elif sum(computer) == 21:
        print("PC wins")
    return sum(player), sum(computer)

print(play_game(player_cards, computer_cards))
check_sum(player_cards, computer_cards)

# if 11 in cards:
#     print("Yes")
