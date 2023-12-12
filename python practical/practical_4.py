# 4. WAP that accepts a character and performs the following

# a. print whether the character is a letter or numeric digit or a special character 
char = input("Enter a character: ")
if char.isalpha():
    print("The character is a letter.")
elif char.isdigit():
    print("The character is a numeric digit.")
elif char.isalnum():
    print("The character is an alphanumeric character.")
else:
    print("The character is a special character.")

#  if the character is a letter, print whether the letter is uppercase or lowercase 
if char.isalpha():
    if char.isupper():
        print("The character is an uppercase letter.")
    elif char.islower():
        print("The character is a lowercase letter.")

# c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output
# is NINE) 
digit_names = {
    '0': 'ZERO',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE'
}
if char.isdigit():
    # Print the name of the numeric digit in text
    digit_name = digit_names.get(char, 'UNKNOWN')
    print(f"The character is {digit_name}.")