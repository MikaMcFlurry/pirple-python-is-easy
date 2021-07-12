row_1 = ["/ ","/ ","/ ","/ ","/ ","/ ","/ ","/"]
row_2 = ["/ ","/ ","/ ","/ ","/ ","/ ","/ ","/"]
row_3 = ["/ ","/ ","/ ","/ ","/ ","/ ","/ ","/"]
row_4 = ["/ ","/ ","/ ","/ ","/ ","/ ","/ ","/"]
row_5 = ["/ ","/ ","/ ","/ ","/ ","/ ","/ ","/"]
row_6 = ["/ ","/ ","/ ","/ ","/ ","/ ","/ ","/"]
colum_number = [" 1", " 2", " 3", " 4", " 5", " 6", " 7"]

def draw_field():
    print("".join(row_1))
    print("".join(row_2))
    print("".join(row_3))
    print("".join(row_4))
    print("".join(row_5))
    print("".join(row_6))
    print("".join(colum_number))
draw_field()

temp_colum = int(input("Choose a colum:\n"))
temp_colum = temp_colum - 1
row_counter = 6
round_counter = 1
print(temp_colum)
print(row_counter)
if row_6[temp_colum] == "/X":
    #print("".join(row_6))
    row_counter = row_counter - 1
    if row_5[temp_colum] == "X" or "O":
        #print("".join(row_5))
        row_counter = row_counter - 1
        if row_4[temp_colum] == "X" or "O":
            #print("".join(row_4))
            row_counter = row_counter - 1
            if row_3[temp_colum] == "X" or "O":
                #print("".join(row_3))
                row_counter = row_counter - 1
                if row_2[temp_colum] == "X" or "O":
                    #print("".join(row_2))
                    row_counter = row_counter - 1
                    if row_1[temp_colum] == "X" or "O":
                        print("Invalid colum! Please try again.")
                        row_counter = row_counter - 1
elif row_counter == 6:
    if round_counter % 2 == 0:
        row_6[temp_colum] == "/X"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
    else:
        row_6[temp_colum] == "/O"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
elif row_counter == 5:
    if round_counter % 2 == 0:
        row_5[temp_colum] == "/X"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
    else:
        row_5[temp_colum] == "/O"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6)) 
elif row_counter == 4:
    if round_counter % 2 == 0:
        row_4[temp_colum] == "/X"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
    else:
        row_4[temp_colum] == "/O"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
elif row_counter == 3:
    if round_counter % 2 == 0:
        row_3[temp_colum] == "/X"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
    else:
        row_3[temp_colum] == "/O"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
elif row_counter == 2:
    if round_counter % 2 == 0:
        row_2[temp_colum] == "/X"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
    else:
        row_2[temp_colum] == "/O"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
elif row_counter == 1:
    if round_counter % 2 == 0:
        row_1[temp_colum] == "/X"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
    else:
        row_1[temp_colum] == "/O"
        print("".join(row_1))
        print("".join(row_2))
        print("".join(row_3))
        print("".join(row_4))
        print("".join(row_5))
        print("".join(row_6))
print(row_counter)