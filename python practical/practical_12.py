# 12. Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations:
t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
half = len(t1)//2
# a. Print half the values of the tuple in one line and the other half in the next line. 
print(t1[:half],t1[half:],sep="\n")

# b. Print another tuple whose values are even numbers in the given tuple
evenList = [i for i in t1 if i%2 ==0]
evenTup = tuple(evenList)
print(evenTup)

# c. Concatenate a tuple t2=(11,13,15) with t1.
t2=(11,13,15)
concattedTup = t1+t2 
print(f"t1 = {t1} \nt2 = {t2} \nConcatenated tuple: ",concattedTup)

# d. Return maximum and minimum value from this tuple
print("Maximum value: {}\nMinimum value: {}".format(max(list(concattedTup)),min(list(concattedTup))))