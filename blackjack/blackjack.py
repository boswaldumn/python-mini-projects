# Simple BlackJack or 21 game (for 2 people - Dealer & Program Operator)
import random
import os
import time


# THE PLANNING PHASE
# Declaring variable for dealer cards
dealer_cards = []
# Declaring variable for player cards
player_cards = []

# Deal the cards
# Dealer Cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has X & \n", dealer_cards[1])


# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have \n", player_cards)


# Sum of the Dealer cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!\n")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!\n")


# Sum of the Player cards
while sum(player_cards) < 21:
    action = str(input("Do you want to stay or hit? (type 'hit' or 'stay')\n"))
    if action == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards) + " from these cards \n", player_cards))
    else:
        print("The Dealer has a total of " + str(sum(dealer_cards)) + " with \n", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with \n", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!\n")
        else: 
            print ("You win!\n")
            break

if sum(player_cards) > 21:
    print("You Busted! Dealer wins.\n")
elif sum(player_cards) == 21:
    print("You have BLACKJACK! You win.")

    # Compare the sums of the cards between Dealer & Player
    # If P card sum is greater than 21 = BUST
    # If P card sum is less than 21 = Option Hit or Stay
    # If P option Stay compare sum of Dealer vs Player
    # If P sum < 21 && > D sum then P wins
    # If P sum < D sum then P loses