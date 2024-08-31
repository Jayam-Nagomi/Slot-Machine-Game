import random

MAX_LINE = 3

MIN_BET=1
MAX_BET=100

ROWS=3
COLS=3

bet_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":4,
    "B":3,
    "C":2,
    "D":1
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)
    return winnings,winning_line


def get_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in bet_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for rows in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[rows], end=" | ")
            else:
                print(column[rows], end="")

        print()
    

def get_deposit(prompt="How much you wanna deposit? "):
    while True:
        dep = input(prompt)
        if dep.isdigit():
            dep = int(dep)
            if dep <= 0:
                print("Amount must be greater than 0")
            else:
                break
        else:
            print("Enter a valid number.")
    return dep
        

def get_bet():
    while True:
        bet = input("How much you wanna bet? ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("Bet must be between 1 to 100")
        else:
            print("Enter a valid number.")
    return bet 

def get_lines():
    while True:
        bet = input("How much lines you wanna bet on (1-3): ")
        if bet.isdigit():
            bet = int(bet)
            if 0 < bet <= MAX_LINE:
                break
            else:
                print("Lines must be 1 to 3")
        else:
            print("Enter a valid number.")
    return bet
    
def spin(balance):
    lines = get_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print("You dont have enough money to bet.")
            answer = input("click enter to bet less or click d to deposit more amount: ")
            if answer=="d":
                dep = get_deposit("How much more you want to deposit? ")
                balance += dep
        else:
            break

    print(f"Your betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_slot_machine(ROWS, COLS, bet_count)
    print_slot_machine(slots)

    winning, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winning>0:
        print(f"You won ${winning}")
        print("You won on line",*winning_lines)
    else:
        print(f"you lost ${total_bet}")

    balance += winning - total_bet
    return balance

def main():
    balance = get_deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Click enter to play (q to quit):")
        if answer == "q":
            break
        else:
            balance = spin(balance)

    print(f"Your left with ${balance}")
    

main()
