# Swap two variable without using 3rd variable
# a = int(input("Enter 1st variable: "))
# b = int(input("Enter 2nd variable: "))
# print(f"before swap a = {a} b = {b}")
# a = a + b
# b = a - b
# a = a - b
# print(f"after swap a = {a} b = {b}")


# Write a Program to extract each digit from an integer in the reverse order.
# b = input("Enter Number: ")
# length = len(str(b))
# for i in range(1,length+1):
#     print(b[-i],end="")

# Write a program that will give you the sum of 3 digits
# a = int(input("Enter 3 digit number: ")) # 345
# sum=0
# for  i in range(len(str(a))):
#     # print(a,sum)
#     x = a%10
#     sum+=x
#     a = a//10   
# print(sum)


# Write a program that will reverse a four digit number.Also it checks whether the reverse is equal to the number itself
# a = int(input("Enter 4 digit number: "))
# b = a
# reverse = 0
# x = a%10
# reverse = reverse + x*1000
# a//=10
# x = a%10
# reverse = reverse + x*100
# a//=10
# x = a%10
# reverse = reverse + x*10
# a//=10
# x = a%10
# reverse = reverse + x*1
# a//=10
# print(reverse)
# print(bool(b==reverse))


# Write a program to find the euclidean distance between two coordinates.
# import math
# x1=float(input("x1: "))
# y1=float(input("y1: "))
# x2=float(input("x2: "))
# y2=float(input("y2: "))
# math.sqrt
# print(f"Distance between point A ({x1},{x2}) and B ({y1},{y2}) = ",round(math.sqrt((x2-x1)**2 + (y2 - y1)**2),2))


# Write a program that will tell whether the given number is divisible by 3 & 6.
# a = int(input("Enter a number: "))
# if a%2==0 and a%3==0:
#     print(f"Given number {a} is divisible by 3 and 6")
# else:
#     print(f"Given number {a} is not divisible by 3 and 6")


# Write a program that will take three digits from the user and add the square of each digit.
# a = int(input("Enter 1st variable: "))
# b = int(input("Enter 2nd variable: "))
# c = int(input("Enter 3rd variable: "))
# print("Adding sqares of each number = ", a**2+b**2+c**2)


# 8. Write a program that will check whether the number is armstrong number or not
# a = int(input("Enter three variable: "))
# new = 0
# b=a
# x = a%10
# new+=x**3
# a//=10
# x = a%10
# new+=x**3
# a//=10
# x = a%10
# new+=x**3
# a//=10
# if b==new:
#     print("The number is armstrong")
# else:
#     print("Not a armstrong")


# 9. Check file is empty or not,Write a program to check if the given file is empty or not
# file = open("file.txt",'r')
# content = file.read()
# if len(content)==0:
#     print("file is empty")
# else:
#     print("file has contenct in it..!")
# file.close()


# 10. Check file is empty or not,Write a program to check if the given file is empty or not
# import os
# size = os.stat("file.txt").st_size
# if size == 0 :
#     print("file is empty: ")
# else:
#     print("file has content in it..!")


# 11. read content from the file
# with open("file.txt") as file:
#     content = file.read()
# print(content)

# 12. read line by line
# with open('file.txt') as file:
#     content = file.read()
#     for i in content.split("\n"):
#         print(i)

# 13. preventing crashes from user input
# while True:
#     print("Enter the 'q' to exit ")
#     a = input("enter the number")
#     if a == 'q':
#         break
#     b = input("Enter 2nd number: ")
#     try:
#         result = int(a)/int(b)
#         print(result)
#     except ZeroDivisionError:
#         print("gaddari karbe..!")
#     except ValueError:
#         print("dhang se value daal")


    
# 14. Print the sum of the current number and the previous number
# prev_num=0
# for i in range(0,11):
#     x = i+prev_num
#     prev_num = i
#     print(x,end=" ")


# 15. Write a python program to search a given number from a list
# a = [2,3,4,5,6,7,8,9,0]
# x = int(input("Enter number to search: "))
# for i in a:
#     if i==x:
#         print("Item found at index",a.index(x))
#         break
# else:
#     print("number not found")


# 16. Create a new list from a two list using the following condition. Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
# l1 = [2,4,6,9,13]
# l2 = [3,5,7,22,20]
# l3=[]
# length = max([len(l1),len(l2)])
# x=0
# while x<length:
#     if l1[x]%2 != 0:
#         l3.append(l1[x])
#     if l2[x]%2 == 0:
#         l3.append(l2[x])
#     x+=1
# print(l3)

# 17. Print multiplication table form 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()

# 18.  Print all the armstrong numbers in the range of 100 to 1000
# armstrong_list = []
# for i in range(100,1000):
#     a = i%10
#     num = i//10
#     b = num%10
#     c = num//10
#     if (a**3)+(b**3)+(c**3) == i:
#         armstrong_list.append(i)
# print(armstrong_list)
        
    


    


