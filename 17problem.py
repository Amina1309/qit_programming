from itertools import product

# Define the mappings for digits 2 and 3
digit_to_letters = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m','n','o'],
    7: ['p','q','r','s'],
    8: ['t','u','v'],
    9: ['w','x','y','z'],
}

# Take user input and validate it
user_input = input("Enter 4 digits in the format 'wxyz': ")

# Extract the 4 digits from the input
try:
    # Convert each character in the input to an integer and check validity
    digits = [int(dino) for dino in user_input]
    if len(digits) == 4 and all(digit in digit_to_letters for digit in digits):
        # Get the corresponding lists of letters for each digit
        lists_of_letters = [digit_to_letters[digit] for digit in digits]
        
        # Generate all possible combinations
        combinations = [''.join(combo) for combo in product(*lists_of_letters)]
        print("Possible combinations:", combinations)
    else:
        print("Invalid input. Please enter only 4 digits from 2 to 9.")
except (IndexError, ValueError):
    print("Kurwa! Please enter exactly 4 digits.")
