def draw_playing_board(rows, columns):
    if rows <= 9 and columns <= 119:    
        real_rows = rows + rows - 1
        real_columns = columns + columns - 1
        for a in range(real_rows):
            if a % 2 == 0:
                for b in range(real_columns):
                    if b % 2 == 0:
                        if b != real_columns - 1:
                            print(" ", end="")

                        else:
                            print("")
                    
                    else:
                        print("|", end="")
            
            else:
                print("-" * real_columns )
        return True

    else:
        return False

print(draw_playing_board(5, 50))