🎰 Spinning Slot Machine Game

Welcome to the Spinning Slot Machine Game! This game simulates a classic slot machine experience, where you deposit money, place bets on multiple lines, spin the reels, and win or lose based on the results. The aim of this project is to improve our understanding of python and functional programming.

📝 Table of Contents
Features
Game Rules
How the Game Works
Setup Instructions
How to Play
Code Logic and Explanation
Demo
Future Improvements
Contributing


🎯 Features
Bet on up to 3 lines in one spin.
Symbols have different values, which affect your winnings.
Real-time balance updates after every spin.
Input validation to ensure smooth gameplay.
Simple, interactive command-line interface.

🎮 Game Rules
Deposit Money: Players begin by depositing an amount to use as their balance.
Place Bets: Choose how many lines (1 to 3) to bet on and the amount to bet per line.
Spin the Machine: The game randomly selects symbols for a 3x3 grid.
Check for Winnings: If symbols align on a bet line, the player wins based on the symbol value multiplied by the bet amount.
Update Balance: Your balance is adjusted based on the winnings or losses.
Continue or Exit: The player can continue spinning as long as they have enough balance or exit anytime.

⚙️ How the Game Works
The slot machine generates a 3x3 grid filled with random symbols.
Winning lines: If symbols align across the columns (horizontally) on a bet line, the player wins.
Winnings: Calculated by multiplying the symbol’s value with the bet amount for that line.
Net Result: The player’s balance is updated after each spin based on the difference between total bet and winnings.
🛠 Setup Instructions
Prerequisites
Python 3.x installed on your system.
A terminal or code editor (like VS Code) for running the program.

Installation
Clone the Repository:
git clone <bet_spinning>
cd <spin>
Run the Game:
python spinning_game.py
🎯 How to Play
Start the Game:
Run the game with python spinning_game.py.
Deposit Money:
Enter the amount you want to deposit as your starting balance:
How much would you like to deposit? $100
Choose the Number of Lines to Bet On:
Select how many lines (1–3) to bet on:
Enter the number of lines to bet on (1-3): 2
Place Your Bet:
Enter how much you want to bet per line
What would you like to bet on each line? $10
Spin the Slot Machine:
The machine will generate a 3x3 grid, displaying the result. For example:
css
A | B | A  
B | B | B  
C | A | C  
You won $40.  
You won on lines: 2
Continue or Exit:
Press Enter to spin again or type 'e' to exit the game:
Press enter to play (e to exit): e
Final Balance:
Once you exit, your final balance will be displayed:
You left with $50

🧠 Code Logic and Explanation
1. Deposit Function (deposit)
Prompts the user to enter a valid deposit amount and returns it.
2. Get Number of Lines (get_number_of_lines)
Allows the player to bet on up to 3 lines, ensuring valid input.
3. Get Bet Amount (get_bet)
Takes a valid bet amount between the minimum and maximum allowed.
4. Spin the Slot Machine (get_slot_machine_spin)
Randomly generates a 3x3 grid by selecting symbols based on predefined counts.
5. Display Grid (print_slot_machine)
Formats and prints the 3x3 grid to the console.
6. Check Winnings (check_winnings)
Checks if the player has any winning lines and calculates the total winnings.
7. Main Loop (main)
Keeps the game running until the player chooses to exit or runs out of money.

🎥 Demo
How much would you like to deposit? $50  
Enter the number of lines to bet on (1-3): 3  
What would you like to bet on each line? $5  
You are betting $5 on 3 lines. Total bet is $15
A | B | A  
B | B | B  
D | C | C  
You won $20.  
You won on lines: 2  
Press enter to play (e to exit): e  
You left with $55

🚀 Future Improvements
Diagonal winning lines to increase the excitement.
Bonus rounds or multipliers for bigger payouts.
Develop a GUI version using libraries like Tkinter or Pygame.
Leaderboard to track player stats like highest balance and most wins.

🤝 Contributing
Contributions are welcome! If you'd like to improve the game or add new features, follow these steps:

Fork the repository.
Create a new branch:
git checkout -b feature-branch
Make your changes and commit:    
git commit -m "Added new feature"
Push to the branch
git push origin feature-branch
Open a Pull Request on GitHub.

📝 Acknowledgements
Inspired by real-world slot machines.
Built with 💻 and ☕ using Python.
