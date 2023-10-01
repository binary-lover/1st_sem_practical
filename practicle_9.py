# 9.WAP to read a file and 

# a. Print the total number of characters, words and lines in the file
file = open("textfile.txt","r")
content = file.read()
print(content.split())
print("Total no of laters in file: ",len([latter for word in content.split() for latter in word]))
print("Total no of words in file: ",len(content.split()))
file.close()

# b. Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count. 
file = open("textfile.txt","r")
content = file.read()
char_list = [latter for word in content.split() for latter in word]
char_set_list = list(set(char_list))
word_count = {}
for i in char_set_list:
    word_count[i] = char_list.count(i)
print(f"frequency of character in the file: {word_count}")
file.close()

# c. Print the words in reverse order
file = open("textfile.txt","r")
content = file.read()
char_list = [word for word in content.split() ]
for i in range(len(char_list)-1,-1,-1):
    print(char_list[i],end=" ")
file.close()

# d. Copy even lines of the file to a file named "File1" and odd lines to another file named "file2"
textfile = open("textfile.txt","r")
file1 = open("file1.txt","w")
file2 = open("file2.txt","w")
content = textfile.readlines()
for i in content:
    if content.index(i) % 2 == 0:
        file2.write(i)
    else:
        file1.write(i)
print("Lines copied sucsessfuly...!\nEven lines in File1 and Odd lines in File2")
textfile.close()
file1.close()
file2.close()

