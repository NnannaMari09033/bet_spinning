import random  # Importing the random module to select random symbols for the slot machine.

# Constants for game settings.
MAX_LINES = 3  # Maximum number of lines a player can bet on.
MAX_BET = 100  # Maximum amount a player can bet on a line.
MIN_BET = 1    # Minimum amount a player can bet on a line.

# Slot machine dimensions.
ROWS = 3  # Number of rows in the slot machine.
COLS = 3  # Number of columns in the slot machine.

# Symbol configurations: Each symbol has a limited count.
symbol_count = {
    "A": 2,  # Symbol "A" appears 2 times.
    "B": 4,  # Symbol "B" appears 4 times.
    "C": 6,  # Symbol "C" appears 6 times.
    "D": 8   # Symbol "D" appears 8 times.
}

# Value of each symbol if it forms a winning combination.
symbol_value = {
    "A": 5,  # "A" pays 5 times the bet.
    "B": 4,  # "B" pays 4 times the bet.
    "C": 3,  # "C" pays 3 times the bet.
    "D": 2   # "D" pays 2 times the bet.
}

def check_winnings(columns, lines, bet, values):
    """Checks if the player wins on any of the bet lines.
    
    Args:
        columns (list): The slot machine columns with symbols.
        lines (int): Number of lines the player bet on.
        bet (int): The amount bet on each line.
        values (dict): The payout value of each symbol.

    Returns:
        tuple: Total winnings and the winning lines.
    """
    winnings = 0  # Store the total winnings.
    winning_lines = []  # Track which lines won.
    
    # Check each line the player bet on.
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol in the first column for the current line.
        
        # Check if all columns have the same symbol in this line.
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # Exit the loop if symbols don't match.
        else:
            # If all symbols in the line match, calculate winnings.
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Record the winning line (1-indexed).
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    """Simulates a slot machine spin and returns the columns with symbols.
    
    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Available symbols and their counts.

    Returns:
        list: A list of columns with randomly selected symbols.
    """
    all_symbols = []  # Store all available symbols based on their count.
    
    # Add each symbol to the list based on its count.
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []  # Store the columns generated for the slot machine.
    
    # Generate symbols for each column.
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Copy the symbol pool for each column.
        
        # Pick a random symbol for each row in the column.
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # Remove the selected symbol to avoid repetition.
            column.append(value)
        
        columns.append(column)  # Add the generated column to the slot machine.
    
    return columns

def print_slot_machine(columns):
    """Displays the slot machine's current spin result."""
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" |")  # Print symbol with separator.
            else:
                print(column[row], end="")  # Print the last symbol without separator.
        print()  # New line after each row.

def deposit():
    """Prompts the player to deposit money and validates the input."""
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break  # Valid deposit amount.
            else:
                print("INVALID. Amount must be greater than zero.")
        else:
            print("Enter a valid number.")
    return amount

def get_number_of_lines():
    """Prompts the player to select the number of lines to bet on."""
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break  # Valid number of lines.
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    """Prompts the player to place a bet for each line and validates it."""
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break  # Valid bet amount.
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    """Handles a single spin of the slot machine.
    
    Args:
        balance (int): The player's current balance.

    Returns:
        int: The net amount won or lost from the spin.
    """
    lines = get_number_of_lines()  # Get the number of lines to bet on.
    
    while True:
        bet = get_bet()  # Get the bet amount per line.
        total_bet = bet * lines  # Calculate the total bet.
        
        if total_bet > balance:
            print(f"Sorry, you do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break  # Valid total bet.
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine.
    print_slot_machine(slots)  # Display the spin result.
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check for winnings.
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)  # Display winning lines.
    
    return winnings - total_bet  # Return the net amount won or lost.

def main():
    """Main function to run the slot machine game."""
    balance = deposit()  # Get the initial deposit from the player.
    
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (e to exit): ")
        if answer == "e":
            break  # Exit the game.
        balance += spin(balance)  # Update the balance after each spin.
    
    print(f"You left with ${balance}")  # Display the final balance.

# Start the game.
main()
