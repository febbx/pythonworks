# write a python program that prompts the user to input a number b/w 1 and 15. the program should then display the corresponding roman numeral for that number

roman_numerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    11: "XI",
    12: "XII",
    13: "XIII",
    14: "XIV",
    15: "XV"
}

user_input = input("enter a number between 1 and 15: ")

if user_input.isdigit():
    
    number = int(user_input)
    
    
    if 1 <= number <= 15:
        print("The Roman numeral for", number, "is:", roman_numerals[number])
    else:
        print("Invalid input. Please enter a number between 1 and 15.")
else:
    print("Invalid input. Please enter a valid integer.")