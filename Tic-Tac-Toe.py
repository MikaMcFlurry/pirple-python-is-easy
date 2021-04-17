Player1 = ()
Player2 = ()
playing = False
current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def draw_field(field):
    global playing
    global current_field
    if playing == False:
        print("\nPlayingfield structure:\n")
        for row in range(5):
            if row % 2 == 0:
                for column in range(5):
                    if column % 2 == 0:
                        if column != 4:
                            print(" ", end=(""))
                        else:
                            if row == 0:
                                print(" ", row + 1)
                            elif row == 2:
                                print(" ", row)
                            else:
                                print(" ", row - 1)
                    else:
                        print("|", end="")

            else:
                print("-----")
        print("1 2 3")

    else:
        for row in range(5):
            if row % 2 == 0:
                practical_row = int(row / 2)
                for column in range(5):
                    if column % 2 == 0:
                        practical_column = int(column / 2)
                        if column != 4:
                            print(field[practical_row][practical_column], end=(""))
                        else:
                            print(field[practical_row][practical_column])
                            
                    else:
                        print("|", end="")

            else:
                print("-----")

def start_game():
    global Player1
    global Player2
    Player1 = input("Type name of player 1:\n")
    Player2 = input("Type name of player 2:\n")
    draw_field(1)
    start = input("\nType in \"start\", to start the game:\n")
    if start == ("start") or start == ("Start") or start == ("START"):
        play_game()


def play_game():
    global playing
    playing = True
    Player = 1
    global current_field
    while(playing):
        if Player == 1:
            print("\nIt's your turn", Player1 + ":")
            row_possition = int(input("Please enter the row\n")) - 1
            if row_possition < 0:
                playing = False
            else:
                column_position = int(input("Please enter the column\n")) - 1
                if column_position < 0:
                    playing = False
                else:
                    if current_field[row_possition][column_position] == " ":
                        current_field[row_possition][column_position] = "X"
                        Player = 2
        else:
            print("\nIt's your turn", Player2 + ":")
            row_possition = int(input("Please enter the row\n")) - 1
            if row_possition < 0:
                playing = False
            else:
                column_position = int(input("Please enter the column\n")) - 1
                if column_position < 0:
                    playing = False
                else:
                    if current_field[row_possition][column_position] == " ":
                        current_field[row_possition][column_position] = "O"
                        Player = 1
        if playing:            
            draw_field(current_field)
            has_won()

def has_won():
    global Player1
    global Player2
    global current_field
    global playing

    if (current_field[0][0] == "X" and current_field[0][1] == "X" and current_field[0][2] == "X" or 
        current_field[0][0] == "X" and current_field[1][0] == "X" and current_field[2][0] == "X" or 
        current_field[0][1] == "X" and current_field[1][1] == "X" and current_field[2][1] == "X" or 
        current_field[0][2] == "X" and current_field[1][2] == "X" and current_field[2][2] == "X" or 
        current_field[1][0] == "X" and current_field[1][1] == "X" and current_field[1][2] == "X" or 
        current_field[2][0] == "X" and current_field[2][1] == "X" and current_field[2][2] == "X" or 
        current_field[0][0] == "X" and current_field[1][1] == "X" and current_field[2][2] == "X" or 
        current_field[0][2] == "X" and current_field[1][1] == "X" and current_field[2][0] == "X"):

        print(Player1 + " has won\nCongrats")
        playing = False
    
    elif (current_field[0][0] == "O" and current_field[0][1] == "O" and  current_field[0][2] == "O" 
        or current_field[0][0] == "O" and current_field[1][0] == "O" and current_field[2][0] == "O" 
        or current_field[0][1] == "O" and current_field[1][1] == "O" and current_field[2][1] == "O"
        or current_field[0][2] == "O" and current_field[1][2] == "O" and current_field[2][2] == "O"
        or current_field[1][0] == "O" and current_field[1][1] == "O" and current_field[1][2] == "O"
        or current_field[2][0] == "O" and current_field[2][1] == "O" and current_field[2][2] == "O"
        or current_field[0][0] == "O" and current_field[1][1] == "O" and current_field[2][2] == "O"
        or current_field[0][2] == "O" and current_field[1][1] == "O" and current_field[2][0] == "O"):

        print(Player2 + " has won\nCongrats")
        playing = False

start_game()
