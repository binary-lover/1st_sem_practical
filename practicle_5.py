# 5. WAP to perform the following operations on a string 
# a. Find the frequency of a character in a string. 
string = input("Enter string : ")

# a. Find the frequency of a character in a string. 
# latter = input("Enter later to find its frequency: ")
# print(f"frequency of {latter} in {string} is ",string.count(latter))

# b. Replace a character by another character in a string. 
# a, b = input("Enter char for replace: "),input("Enter char to replace with: ")
# replace = string.replace(a,b)
# print(f"replaced string is {replace}")

# c. Remove the first occurrence of a character from a string. 
char_to_remove = input("Enter the character to remove: ")
modified_string = string.replace(char_to_remove, '', 1)
print("Modified string:", modified_string)



