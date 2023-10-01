# 11. Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys. 
def dict_for_num_cubes(list_of_num):
    dict1 = {}
    for num in list_of_num:
        dict1[num]= int(num)**3
    print("Dict with the number and its cube:",dict1,sep="\n")

num_list = list(input("enter list item with a space (Note: wtire only integers ): ").split())
dict_for_num_cubes(num_list)