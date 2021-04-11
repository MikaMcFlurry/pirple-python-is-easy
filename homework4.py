my_unique_list = []
my_leftovers = []

def add_to_unique_list(input):
    if input in my_unique_list:
        return False
    
    my_unique_list.append(input)
    return True  

def add_to_list(input):
    if not add_to_unique_list(input):
        my_leftovers.append(input)
        return False
    return True

add_to_list(4)
add_to_list(4)
add_to_list(3)
add_to_list(2)
result = add_to_list(1)
print(result)
print(my_unique_list)
print(my_leftovers)
result = add_to_list(3)
print(result)
print(my_unique_list)
print(my_leftovers)