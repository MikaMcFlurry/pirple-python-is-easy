song_describtion = {
    "Song": "Sonne",
    "Artist": "Rammstein",
    "Genre": "Metal",
    "Album": "Mutter",
    "Releasyear": 2001,
    "Duration": 4.53,
    "Spotifystreams": 150118217
}


def guess_song_describtion(key, value):
    if key in song_describtion and value == song_describtion[key]:
        return print(True)
    else:
        return print(False)


while True:
    print("In this game you can guess the answer of following facts:\n Song, Artist, Genre, Album, Releasyear, Duration or Spotifystreams\n How to play:\n 1. Type in one of the facts\n 2. Type in your guess\n If your guess was RIGHT it will say True and you can play again\n If your guess was WRONG it will say False and you can play again\n If you want to exit the game or see the solutions type in Exit for key\n Have fun")
    key = input("Type in a key:\n")
    if key == "Exit":
        break
    value = input("Type in your guess:\n")
    guess_song_describtion(key, value)

for key in song_describtion:
    print(key, ":", song_describtion[key])
