# Used for clearing the console
from __future__ import print_function
cls = lambda: print("\033c", end='')

import sys
import random
from art import logo

# Returns a random element from a list mylist, used for drawing random cards
def deal_card(mylist):
  return mylist[random.randint(0, len(mylist) - 1)]

def calculate_score(mycards):
  score = 0
  score = sum(mycards)
  
  # BlackJack
  if score == 21 and len(mycards) == 2:
    return 0

  if score > 21 and 11 in mycards:
    mycards.remove(11) # search for the first element and removes it
    mycards.append(1)
    score -= 10
      
  return score

# Function for comparing scores after user hit pass
def compare_after_user_pass(user_score, computer_score):
  
  if computer_score > 21:
    print("computer went overboard, you win")
  else:
    if computer_score == user_score:
      print("It's a draw")
    elif computer_score > user_score:
      print("Computer wins")
    elif computer_score < user_score:
      print("You win!!")

############## Main function that is called ##############################
def blackjack():

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  user_cards = []
  computer_cards = []

  user_score = 0
  computer_score = 0
  
  # Ask the user if he wants to play, it's called everytime in the beginning
  user_choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") 
  if user_choice == 'n':
    print("Goodbye!! :-)")
    # return 0
    sys.exit() # To be sure that we exiting the program
  
  # Clear console
  cls()
  # Print logo
  print(logo)   
  
  # We create a starting hand for both user and computer, with two random values
  starting_counter = 0
  while starting_counter < 2:
    user_cards.append(deal_card(cards))
    computer_cards.append(deal_card(cards))
    starting_counter += 1
 
  ##############################################################
  # This logic in the loop works for the BEGINNING hand also
  user_is_drawing_cards = True
  while user_is_drawing_cards:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    # Print user's first two cards and beginning score
    print(f"Your cards: {user_cards}, current score: {user_score}")
    # Print computers fist card
    print(f"Computer's first card: {computer_cards[0]} ")
    
    # Check if computer or user have BlackJack, in the first hand, first two cards that are dealt
    if user_score == 0 or computer_score == 0:   
      if computer_score == 0:
        print("You lose, computer has blackjack")
        blackjack()
      else:
        print("You win with blackjack!")
        blackjack()
    # Is user's score over 21, game ends
    elif user_score > 21:
        print("You lose, you went overboard")
        blackjack()
  
    # Ask the user if they want to get another card
    else:
      user_wants_draw = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_wants_draw == 'y':
        user_cards.append(deal_card(cards))
      if user_wants_draw == 'n':
        user_is_drawing_cards = False # Exit the loop
        
  # print(f"computer score now is {computer_score}")

  # if computer's first hand score is < 17, computer keeps drawing cards and compares after is > 17
  while computer_score < 17:    
    computer_cards.append(deal_card(cards))
    computer_score = calculate_score(computer_cards)

  print("\n")
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  compare_after_user_pass(user_score, computer_score)  
  blackjack()
  
# This is where we begin
blackjack()

