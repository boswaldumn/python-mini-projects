# BlackJack or 21 game
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
        print("Dealer has X & ", dealer_cards[1])


# Player Cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have ", player_cards)


    # Sum of the Dealer cards
    # Sum of the Player cards
    # Compare the sums of the cards between Dealer & Player
    # If P card sum is greater than 21 = BUST
    # If P card sum is less than 21 = Option Hit or Stay
    # If P option Stay compare sum of Dealer vs Player
    # If P sum < 21 && > D sum then P wins
    # If P sum < D sum then P loses