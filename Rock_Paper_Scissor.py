# Step 1: Create a class for the Game
import random

class RockPaperScissorsGame:
    # Step 2: Initialize the class with options
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissor']

    # Step 3: Method to get the computer's choice
    def get_computer_choice(self):
        return random.choice(self.choices)

    # Step 4: Method to get the player's choice
    def get_player_choice(self):
        choice = input("Enter rock, paper, or scissors: ").lower()
        while choice not in self.choices:
            choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
        return choice

    # Step 5: Method to determine the winner
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    # Step 6: Method to play the game
    def play(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = self.determine_winner(player_choice, computer_choice)
        print(result)

# Step 7: Create an instance of the game and start playing
if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play()
