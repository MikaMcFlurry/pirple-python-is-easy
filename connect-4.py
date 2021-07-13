row_1 = ["/  ","/  ","/  ","/  ","/  ","/  ","/  ","/"]
row_2 = ["/  ","/  ","/  ","/  ","/  ","/  ","/  ","/"]
row_3 = ["/  ","/  ","/  ","/  ","/  ","/  ","/  ","/"]
row_4 = ["/  ","/  ","/  ","/  ","/  ","/  ","/  ","/"]
row_5 = ["/  ","/  ","/  ","/  ","/  ","/  ","/  ","/"]
row_6 = ["/  ","/  ","/  ","/  ","/  ","/  ","/  ","/"]
column_number = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 "]
round_counter = 1

def get_column():
    global temp_column
    global row_counter
    global round_counter
    ask_for_column = "Player 1 choose a colum:\n"
    if round_counter % 2 != 0:
           ask_for_column = "Player 1 choose a colum:\n"
    else:
        ask_for_column = "Player 2 choose a colum:\n"
    temp_column = int(input(ask_for_column))
    temp_column = temp_column - 1
    row_counter = 6
    creat_new_field()

def draw_field():
    print("".join(row_1))
    print("".join(row_2))
    print("".join(row_3))
    print("".join(row_4))
    print("".join(row_5))
    print("".join(row_6))
    print("".join(column_number))
    print("Player 1 = O\nPlayer 2 = X")
    get_column()

def draw_new_field():
    global round_counter
    if row_counter == 6:
        if round_counter % 2 == 0:
            row_6[temp_column] = "/X "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
        else:
            row_6[temp_column] = "/O "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
    elif row_counter == 5:
        if round_counter % 2 == 0:
            row_5[temp_column] = "/X "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
        else:
            row_5[temp_column] = "/O "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number)) 
    elif row_counter == 4:
        if round_counter % 2 == 0:
            row_4[temp_column] = "/X "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
        else:
            row_4[temp_column] = "/O "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
    elif row_counter == 3:
        if round_counter % 2 == 0:
            row_3[temp_column] = "/X "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
        else:
            row_3[temp_column] = "/O "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
    elif row_counter == 2:
        if round_counter % 2 == 0:
            row_2[temp_column] = "/X "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
        else:
            row_2[temp_column] = "/O "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
    elif row_counter == 1:
        if round_counter % 2 == 0:
            row_1[temp_column] = "/X "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
        else:
            row_1[temp_column] = "/O "
            print("Player 1 = O\nPlayer 2 = X")
            print("".join(row_1))
            print("".join(row_2))
            print("".join(row_3))
            print("".join(row_4))
            print("".join(row_5))
            print("".join(row_6))
            print("".join(column_number))
    round_counter = round_counter + 1
    check_if_winner()

def creat_new_field():
    global row_counter
    if "/O " in row_6[temp_column] or "/X " in row_6[temp_column]:
        row_counter = row_counter - 1
        if "/O " in row_5[temp_column] or "/X " in row_5[temp_column]:
            row_counter = row_counter - 1
            if "/O " in row_4[temp_column] or "/X " in row_4[temp_column]:
                row_counter = row_counter - 1
                if "/O " in row_3[temp_column] or "/X " in row_3[temp_column]:
                    row_counter = row_counter - 1
                    if "/O " in row_2[temp_column] or "/X " in row_2[temp_column]:
                        row_counter = row_counter - 1
                        if "/O " in row_1[temp_column] or "/X " in row_1[temp_column]:
                                    print("Invalid colum! Please try again.")
                                    row_counter = row_counter - 1
                                    get_column()
                        else:
                            draw_new_field()
                    else:
                        draw_new_field()
                else:
                    draw_new_field()
            else:
                draw_new_field()
        else:
            draw_new_field()                    
    else:
        draw_new_field() 

def check_if_winner():
    if ("/X " in row_6[0] and "/X " in row_6[1] and "/X " in row_6[2] and "/X " in row_6[3] or
    "/X " in row_6[1] and "/X " in row_6[2] and "/X " in row_6[3] and "/X " in row_6[4] or
    "/X " in row_6[2] and "/X " in row_6[3] and "/X " in row_6[4] and "/X " in row_6[5] or
    "/X " in row_6[3] and "/X " in row_6[4] and "/X " in row_6[5] and "/X " in row_6[6] or
    "/X " in row_5[0] and "/X " in row_5[1] and "/X " in row_5[2] and "/X " in row_5[3] or
    "/X " in row_5[1] and "/X " in row_5[2] and "/X " in row_5[3] and "/X " in row_5[4] or 
    "/X " in row_5[2] and "/X " in row_5[3] and "/X " in row_5[4] and "/X " in row_5[5] or 
    "/X " in row_5[3] and "/X " in row_5[4] and "/X " in row_5[5] and "/X " in row_5[6] or 
    "/X " in row_4[0] and "/X " in row_4[1] and "/X " in row_4[2] and "/X " in row_4[3] or 
    "/X " in row_4[1] and "/X " in row_4[2] and "/X " in row_4[3] and "/X " in row_4[4] or
    "/X " in row_4[2] and "/X " in row_4[3] and "/X " in row_4[4] and "/X " in row_4[5] or 
    "/X " in row_4[3] and "/X " in row_4[4] and "/X " in row_4[5] and "/X " in row_4[6] or 
    "/X " in row_3[0] and "/X " in row_3[1] and "/X " in row_3[2] and "/X " in row_3[3] or 
    "/X " in row_3[1] and "/X " in row_3[2] and "/X " in row_3[3] and "/X " in row_3[4] or 
    "/X " in row_3[2] and "/X " in row_3[3] and "/X " in row_3[4] and "/X " in row_3[5] or 
    "/X " in row_3[3] and "/X " in row_3[4] and "/X " in row_3[5] and "/X " in row_3[6] or 
    "/X " in row_2[0] and "/X " in row_2[1] and "/X " in row_2[2] and "/X " in row_2[3] or 
    "/X " in row_2[1] and "/X " in row_2[2] and "/X " in row_2[3] and "/X " in row_2[4] or  
    "/X " in row_2[2] and "/X " in row_2[3] and "/X " in row_2[4] and "/X " in row_2[5] or 
    "/X " in row_2[3] and "/X " in row_2[4] and "/X " in row_2[5] and "/X " in row_2[6] or  
    "/X " in row_1[0] and "/X " in row_1[1] and "/X " in row_1[2] and "/X " in row_1[3] or 
    "/X " in row_1[1] and "/X " in row_1[2] and "/X " in row_1[3] and "/X " in row_1[4] or 
    "/X " in row_1[2] and "/X " in row_1[3] and "/X " in row_1[4] and "/X " in row_1[5] or 
    "/X " in row_1[3] and "/X " in row_1[4] and "/X " in row_1[5] and "/X " in row_1[6] or 
    "/X " in row_6[0] and "/X " in row_5[1] and "/X " in row_4[2] and "/X " in row_3[3] or 
    "/X " in row_5[0] and "/X " in row_4[1] and "/X " in row_3[2] and "/X " in row_2[3] or 
    "/X " in row_4[0] and "/X " in row_3[1] and "/X " in row_2[2] and "/X " in row_1[3] or 
    "/X " in row_6[1] and "/X " in row_5[2] and "/X " in row_4[3] and "/X " in row_3[4] or 
    "/X " in row_5[1] and "/X " in row_4[2] and "/X " in row_3[3] and "/X " in row_2[4] or 
    "/X " in row_4[1] and "/X " in row_3[2] and "/X " in row_2[3] and "/X " in row_1[4] or 
    "/X " in row_6[2] and "/X " in row_5[3] and "/X " in row_4[4] and "/X " in row_3[5] or 
    "/X " in row_5[2] and "/X " in row_4[3] and "/X " in row_3[4] and "/X " in row_2[5] or 
    "/X " in row_4[2] and "/X " in row_3[3] and "/X " in row_2[4] and "/X " in row_1[5] or 
    "/X " in row_6[3] and "/X " in row_5[4] and "/X " in row_4[5] and "/X " in row_3[6] or 
    "/X " in row_5[3] and "/X " in row_4[4] and "/X " in row_3[5] and "/X " in row_2[6] or 
    "/X " in row_4[3] and "/X " in row_3[4] and "/X " in row_2[5] and "/X " in row_1[6] or 
    "/X " in row_6[3] and "/X " in row_5[2] and "/X " in row_4[1] and "/X " in row_3[0] or 
    "/X " in row_5[3] and "/X " in row_4[2] and "/X " in row_3[1] and "/X " in row_2[0] or 
    "/X " in row_4[3] and "/X " in row_3[2] and "/X " in row_2[1] and "/X " in row_1[0] or 
    "/X " in row_6[6] and "/X " in row_5[5] and "/X " in row_4[4] and "/X " in row_3[3] or 
    "/X " in row_5[6] and "/X " in row_4[5] and "/X " in row_3[4] and "/X " in row_2[3] or 
    "/X " in row_4[6] and "/X " in row_3[5] and "/X " in row_2[4] and "/X " in row_1[3] or 
    "/X " in row_6[5] and "/X " in row_5[4] and "/X " in row_4[3] and "/X " in row_3[2] or 
    "/X " in row_5[5] and "/X " in row_4[4] and "/X " in row_3[3] and "/X " in row_2[2] or 
    "/X " in row_4[5] and "/X " in row_3[4] and "/X " in row_2[3] and "/X " in row_1[2] or 
    "/X " in row_6[4] and "/X " in row_5[3] and "/X " in row_4[2] and "/X " in row_3[1] or 
    "/X " in row_5[4] and "/X " in row_4[3] and "/X " in row_3[2] and "/X " in row_2[1] or 
    "/X " in row_4[4] and "/X " in row_3[3] and "/X " in row_2[2] and "/X " in row_1[1] or 
    "/X " in row_6[0] and "/X " in row_5[0] and "/X " in row_4[0] and "/X " in row_3[0] or 
    "/X " in row_5[0] and "/X " in row_4[0] and "/X " in row_3[0] and "/X " in row_2[0] or 
    "/X " in row_4[0] and "/X " in row_3[0] and "/X " in row_2[0] and "/X " in row_1[0] or 
    "/X " in row_6[1] and "/X " in row_5[1] and "/X " in row_4[1] and "/X " in row_3[1] or 
    "/X " in row_5[1] and "/X " in row_4[1] and "/X " in row_3[1] and "/X " in row_2[1] or 
    "/X " in row_4[1] and "/X " in row_3[1] and "/X " in row_2[1] and "/X " in row_1[1] or 
    "/X " in row_6[2] and "/X " in row_5[2] and "/X " in row_4[2] and "/X " in row_3[2] or 
    "/X " in row_5[2] and "/X " in row_4[2] and "/X " in row_3[0] and "/X " in row_2[2] or 
    "/X " in row_4[2] and "/X " in row_3[2] and "/X " in row_2[0] and "/X " in row_1[2] or 
    "/X " in row_6[3] and "/X " in row_5[3] and "/X " in row_4[3] and "/X " in row_3[3] or 
    "/X " in row_5[3] and "/X " in row_4[3] and "/X " in row_3[3] and "/X " in row_2[3] or 
    "/X " in row_4[3] and "/X " in row_3[3] and "/X " in row_2[3] and "/X " in row_1[3] or 
    "/X " in row_6[4] and "/X " in row_5[4] and "/X " in row_4[4] and "/X " in row_3[4] or 
    "/X " in row_5[4] and "/X " in row_4[4] and "/X " in row_3[4] and "/X " in row_2[4] or 
    "/X " in row_4[4] and "/X " in row_3[4] and "/X " in row_2[4] and "/X " in row_1[4] or 
    "/X " in row_6[5] and "/X " in row_5[5] and "/X " in row_4[5] and "/X " in row_3[5] or 
    "/X " in row_5[5] and "/X " in row_4[5] and "/X " in row_3[5] and "/X " in row_2[5] or 
    "/X " in row_4[5] and "/X " in row_3[5] and "/X " in row_2[5] and "/X " in row_1[5] or 
    "/X " in row_6[6] and "/X " in row_5[6] and "/X " in row_4[6] and "/X " in row_3[6] or 
    "/X " in row_5[6] and "/X " in row_4[6] and "/X " in row_3[6] and "/X " in row_2[6] or 
    "/X " in row_4[6] and "/X " in row_3[6] and "/X " in row_2[6] and "/X " in row_1[6] or 
    "/O " in row_6[0] and "/O " in row_6[1] and "/O " in row_6[2] and "/O " in row_6[3] or 
    "/O " in row_6[1] and "/O " in row_6[2] and "/O " in row_6[3] and "/O " in row_6[4] or 
    "/O " in row_6[2] and "/O " in row_6[3] and "/O " in row_6[4] and "/O " in row_6[5] or 
    "/O " in row_6[3] and "/O " in row_6[4] and "/O " in row_6[5] and "/O " in row_6[6] or 
    "/O " in row_5[0] and "/O " in row_5[1] and "/O " in row_5[2] and "/O " in row_5[3] or 
    "/O " in row_5[1] and "/O " in row_5[2] and "/O " in row_5[3] and "/O " in row_5[4] or 
    "/O " in row_5[2] and "/O " in row_5[3] and "/O " in row_5[4] and "/O " in row_5[5] or 
    "/O " in row_5[3] and "/O " in row_5[4] and "/O " in row_5[5] and "/O " in row_5[6] or 
    "/O " in row_4[0] and "/O " in row_4[1] and "/O " in row_4[2] and "/O " in row_4[3] or 
    "/O " in row_4[1] and "/O " in row_4[2] and "/O " in row_4[3] and "/O " in row_4[4] or 
    "/O " in row_4[2] and "/O " in row_4[3] and "/O " in row_4[4] and "/O " in row_4[5] or 
    "/O " in row_4[3] and "/O " in row_4[4] and "/O " in row_4[5] and "/O " in row_4[6] or 
    "/O " in row_3[0] and "/O " in row_3[1] and "/O " in row_3[2] and "/O " in row_3[3] or 
    "/O " in row_3[1] and "/O " in row_3[2] and "/O " in row_3[3] and "/O " in row_3[4] or 
    "/O " in row_3[2] and "/O " in row_3[3] and "/O " in row_3[4] and "/O " in row_3[5] or 
    "/O " in row_3[3] and "/O " in row_3[4] and "/O " in row_3[5] and "/O " in row_3[6] or 
    "/O " in row_2[0] and "/O " in row_2[1] and "/O " in row_2[2] and "/O " in row_2[3] or 
    "/O " in row_2[1] and "/O " in row_2[2] and "/O " in row_2[3] and "/O " in row_2[4] or 
    "/O " in row_2[2] and "/O " in row_2[3] and "/O " in row_2[4] and "/O " in row_2[5] or 
    "/O " in row_2[3] and "/O " in row_2[4] and "/O " in row_2[5] and "/O " in row_2[6] or 
    "/O " in row_1[0] and "/O " in row_1[1] and "/O " in row_1[2] and "/O " in row_1[3] or 
    "/O " in row_1[1] and "/O " in row_1[2] and "/O " in row_1[3] and "/O " in row_1[4] or 
    "/O " in row_1[2] and "/O " in row_1[3] and "/O " in row_1[4] and "/O " in row_1[5] or 
    "/O " in row_1[3] and "/O " in row_1[4] and "/O " in row_1[5] and "/O " in row_1[6] or
    "/O " in row_6[0] and "/O " in row_5[1] and "/O " in row_4[2] and "/O " in row_3[3] or 
    "/O " in row_5[0] and "/O " in row_4[1] and "/O " in row_3[2] and "/O " in row_2[3] or 
    "/O " in row_4[0] and "/O " in row_3[1] and "/O " in row_2[2] and "/O " in row_1[3] or 
    "/O " in row_6[1] and "/O " in row_5[2] and "/O " in row_4[3] and "/O " in row_3[4] or 
    "/O " in row_5[1] and "/O " in row_4[2] and "/O " in row_3[3] and "/O " in row_2[4] or 
    "/O " in row_4[1] and "/O " in row_3[2] and "/O " in row_2[3] and "/O " in row_1[4] or 
    "/O " in row_6[2] and "/O " in row_5[3] and "/O " in row_4[4] and "/O " in row_3[5] or 
    "/O " in row_5[2] and "/O " in row_4[3] and "/O " in row_3[4] and "/O " in row_2[5] or 
    "/O " in row_4[2] and "/O " in row_3[3] and "/O " in row_2[4] and "/O " in row_1[5] or 
    "/O " in row_6[3] and "/O " in row_5[4] and "/O " in row_4[5] and "/O " in row_3[6] or 
    "/O " in row_5[3] and "/O " in row_4[4] and "/O " in row_3[5] and "/O " in row_2[6] or 
    "/O " in row_4[3] and "/O " in row_3[4] and "/O " in row_2[5] and "/O " in row_1[6] or 
    "/O " in row_6[3] and "/O " in row_5[2] and "/O " in row_4[1] and "/O " in row_3[0] or 
    "/O " in row_5[3] and "/O " in row_4[2] and "/O " in row_3[1] and "/O " in row_2[0] or 
    "/O " in row_4[3] and "/O " in row_3[2] and "/O " in row_2[1] and "/O " in row_1[0] or 
    "/O " in row_6[6] and "/O " in row_5[5] and "/O " in row_4[4] and "/O " in row_3[3] or 
    "/O " in row_5[6] and "/O " in row_4[5] and "/O " in row_3[4] and "/O " in row_2[3] or 
    "/O " in row_4[6] and "/O " in row_3[5] and "/O " in row_2[4] and "/O " in row_1[3] or 
    "/O " in row_6[5] and "/O " in row_5[4] and "/O " in row_4[3] and "/O " in row_3[2] or 
    "/O " in row_5[5] and "/O " in row_4[4] and "/O " in row_3[3] and "/O " in row_2[2] or 
    "/O " in row_4[5] and "/O " in row_3[4] and "/O " in row_2[3] and "/O " in row_1[2] or 
    "/O " in row_6[4] and "/O " in row_5[3] and "/O " in row_4[2] and "/O " in row_3[1] or 
    "/O " in row_5[4] and "/O " in row_4[3] and "/O " in row_3[2] and "/O " in row_2[1] or 
    "/O " in row_4[4] and "/O " in row_3[3] and "/O " in row_2[2] and "/O " in row_1[1] or 
    "/O " in row_6[0] and "/O " in row_5[0] and "/O " in row_4[0] and "/O " in row_3[0] or 
    "/O " in row_5[0] and "/O " in row_4[0] and "/O " in row_3[0] and "/O " in row_2[0] or 
    "/O " in row_4[0] and "/O " in row_3[0] and "/O " in row_2[0] and "/O " in row_1[0] or 
    "/O " in row_6[1] and "/O " in row_5[1] and "/O " in row_4[1] and "/O " in row_3[1] or 
    "/O " in row_5[1] and "/O " in row_4[1] and "/O " in row_3[1] and "/O " in row_2[1] or 
    "/O " in row_4[1] and "/O " in row_3[1] and "/O " in row_2[1] and "/O " in row_1[1] or 
    "/O " in row_6[2] and "/O " in row_5[2] and "/O " in row_4[2] and "/O " in row_3[2] or 
    "/O " in row_5[2] and "/O " in row_4[2] and "/O " in row_3[0] and "/O " in row_2[2] or 
    "/O " in row_4[2] and "/O " in row_3[2] and "/O " in row_2[0] and "/O " in row_1[2] or 
    "/O " in row_6[3] and "/O " in row_5[3] and "/O " in row_4[3] and "/O " in row_3[3] or 
    "/O " in row_5[3] and "/O " in row_4[3] and "/O " in row_3[3] and "/O " in row_2[3] or 
    "/O " in row_4[3] and "/O " in row_3[3] and "/O " in row_2[3] and "/O " in row_1[3] or 
    "/O " in row_6[4] and "/O " in row_5[4] and "/O " in row_4[4] and "/O " in row_3[4] or 
    "/O " in row_5[4] and "/O " in row_4[4] and "/O " in row_3[4] and "/O " in row_2[4] or 
    "/O " in row_4[4] and "/O " in row_3[4] and "/O " in row_2[4] and "/O " in row_1[4] or 
    "/O " in row_6[5] and "/O " in row_5[5] and "/O " in row_4[5] and "/O " in row_3[5] or 
    "/O " in row_5[5] and "/O " in row_4[5] and "/O " in row_3[5] and "/O " in row_2[5] or 
    "/O " in row_4[5] and "/O " in row_3[5] and "/O " in row_2[5] and "/O " in row_1[5] or 
    "/O " in row_6[6] and "/O " in row_5[6] and "/O " in row_4[6] and "/O " in row_3[6] or 
    "/O " in row_5[6] and "/O " in row_4[6] and "/O " in row_3[6] and "/O " in row_2[6] or 
    "/O " in row_4[6] and "/O " in row_3[6] and "/O " in row_2[6] and "/O " in row_1[6]):

        if round_counter % 2 == 0:
            print("Player 1 has won!")
        else:
            print("Player 2 has won!")
    else:
        get_column()

draw_field()
