
import random


def get_choices():
    player_choice = input("Choose Rock, Paper, or Scissors")

    return player_choice
def get_computer_choice():

    computer_choice = ["rock","paper","scissors"]
    return random.choice(computer_choice)
def winner(player_choice,computer_choice):
    if player_choice == computer_choice:
            return "you lose !"
    elif (
            (player_choice == "rock" and computer_choice == "scissors") or
            (player_choice == "paper" and computer_choice == "rock") or
            (player_choice == "scissors" and computer_choice =="Rock")
        ):
         return "you win"
    else:
         return "loser :o "
    
def main():
     print("Welcome to the game ")

     while True:
          player_choice = get_choices
          computer_choice =get_computer_choice

          print("..... you chose:{player_choice}")
          print("......computer chose: {computer_choice}")
     winner = determine_winner(player_choice , computer_choice)

