# 7)Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list. If the second string is not present in the first string then it should return -1.

def find_occurrences(main_string, sub_string):
    occurrences = []
    start_index = 0
    
    while start_index < len(main_string):
        index = main_string.find(sub_string,start_index)
        if index == -1:
            break
        occurrences.append(index)
        start_index = index+1
    if occurrences:
        return occurrences
    else:
        return -1
        
main_string = "he is good he is bad he is a good bad boy"
sub_string = "is"
result = find_occurrences(main_string, sub_string)
print("Occurrences of '{}' in '{}':".format(sub_string, main_string))
print(result)
