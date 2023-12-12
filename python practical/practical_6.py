# 6. WAP to swap the first n characters of two strings. 
def swap_first_n_characters(str1, str2, n):
    if n <= 0:
        return "Invalid value for n"
    
    if n > len(str1) or n > len(str2):
        return "n exceeds the length of one or both strings"
    
    swapped_str1 = str2[:n] + str1[n:]
    swapped_str2 = str1[:n] + str2[n:]
    
    return swapped_str1, swapped_str2

str1 = "hello"
str2 = "world"
n = 3
result_str1, result_str2 = swap_first_n_characters(str1, str2, n)
print("Swapped strings:")
print(result_str1)  
print(result_str2)  
