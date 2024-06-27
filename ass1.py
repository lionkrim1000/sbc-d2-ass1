import random

class SwertresGame:
    def __init__(self):
        self.player_numbers = []
        self.computer_numbers = []

    def get_player_numbers(self):
        while True:
            try:
                player_input = input("Enter three numbers (0-9) separated by spaces: ").split()
                if len(player_input) != 3:
                    raise ValueError("Please enter exactly three numbers.")
                
                self.player_numbers = [int(num) for num in player_input]
                if any(num < 0 or num > 9 for num in self.player_numbers):
                    raise ValueError("Numbers must be between 0 and 9.")
                
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def generate_computer_numbers(self):
        self.computer_numbers = [random.randint(0, 9) for _ in range(3)]

    def determine_result(self):
        if self.player_numbers == self.computer_numbers:
            return "Win"
        elif sorted(self.player_numbers) == sorted(self.computer_numbers):
            return "Partially Win"
        else:
            return "Lose"

    def display_result(self, result):
        print(f"Your numbers: {self.player_numbers}")
        print(f"Computer's numbers: {self.computer_numbers}")
        print(f"Result: You {result}!\n")

    def play(self):
        print("Welcome to the Swertres Game!")
        
        while True:
            self.get_player_numbers()
            self.generate_computer_numbers()
            result = self.determine_result()
            self.display_result(result)
            
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                break

# Run the game
if __name__ == "__main__":
    game = SwertresGame()
    game.play()
