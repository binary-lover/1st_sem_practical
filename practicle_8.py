# 8. WAP to create a list of the cubes of only the even integers appearing in the input list (may have elements of other types also) using the following:

# a:'for' loop
rng = int(input("enter the no of numbers wnat to input: "))
inp_list = []
cube_list = []
for i in range(rng):
    inp_list.append(input(f"Enter num-{i} : "))
    if inp_list[i].isdigit() and int(inp_list[i]) %2 ==0:
            cube_list.append(int(inp_list[i])**3)
print(inp_list,cube_list) 


# b. list comprehension
inp_list2 = list(input("enter list item with a space").split())
print("your input list: ",inp_list2)
inp_list3 = [int(i) for i in inp_list2 if i.isdigit()]
cube_list2 = [item ** 3 for item in  inp_list3 if isinstance(item, int) and item % 2 == 0]
print("Using list conprehensio: ",cube_list2)
 

