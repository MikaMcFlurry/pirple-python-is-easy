def string_integer_comparator (a, b, c):
    return int (a) == int (b) or int (a) == int (c) or int (b) == int (c) 

print(string_integer_comparator("1", 2, "3"))