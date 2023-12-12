# 13. WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters.
def handleName(name):
    try:
        if any(char.isdigit() for char in name):
            raise ValueError("Name can't contain digits")
        elif not name.isalpha():
            raise ValueError("Name con't contain spechil character")
        print("Name Entered: ",name)
    except ValueError as e:
        print("Error",e)

name = input("Enter your name: ")
handleName(name)

