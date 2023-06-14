'''
    A game of Blackjack. Lookup the rules online or read a book.
'''
from art import logo
import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(hand):
    hand.append(random.choice(cards))
    return hand

def play_game(player, computer):
    player = deal_card(player)
    player = deal_card(player)
    computer = deal_card(computer)
    computer = deal_card(computer)
    return player, computer

def check_sum(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    elif 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)

def compare(p_score, c_score):
    if p_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Computer won with Blackjack"
    elif p_score == 0:
        return "Player won with Blackjack"
    elif p_score > 21:
        return "Player lost"
    elif c_score > 21:
        return "Computer lost"
    elif p_score > c_score:
        return "Player wins with higher points"
    else:
        return "Computer wins with higher points"
def start_game():
    print(logo)
    computer_cards = []
    player_cards = []
    game_over = False

    play_game(player_cards, computer_cards)

    while game_over == False:
        playerScore = check_sum(player_cards)
        computerScore = check_sum(computer_cards)
        print(f"Player cards: {player_cards}, Player score: {playerScore}")
        print(f"Computer's visible card: {computer_cards[0]}")

        if playerScore == 0 or computerScore == 0 or playerScore > 21:
            game_over = True
        else:
            contunue_game = input("Type y to get another card or n to pass: ")
            if contunue_game == "y":
                deal_card(player_cards)
            else:
                game_over = True
        print()

    while computerScore != 0 and computerScore < 17:
        deal_card(computer_cards)
        computerScore = check_sum(computer_cards)

    print(compare(playerScore, computerScore))
    print()
    print(f"---Final results---\nPlayer score: {playerScore}, cards: {player_cards}\nComputer score: {computerScore}, cards: {computer_cards}")

while input("Play the game? y/n: ") == "y":
    system("clear")
    start_game()
    