def equality_comparer (a, b, c):
    return a == b or a == c or b == c 

print(equality_comparer(1, 5, 1))

def string_integer_comparer (a, b, c):
    return a == b or a == c or b == c 

print(string_integer_comparer(int ("1"), int (2), int ("3")))