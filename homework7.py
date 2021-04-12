languages = ["english", "English", "ENGLISH", "englisch", "Englisch",
             "ENGLISCH", "german", "German", "GERMAN", "deutsch", "Deutsch", "DEUTSCH"]
language = ""

song_description_english = {
    "Song": "Sonne",
    "Artist": "Rammstein",
    "Genre": "Metal",
    "Album": "Mutter",
    "Release Year": 2001,
    "Duration": "4:32",
    "Spotify Streams": 150560966
}

song_description_german = {
    "Lied": "Sonne",
    "Künstler": "Rammstein",
    "Genre": "Metal",
    "Album": "Mutter",
    "Erscheinungsjahr": 2001,
    "Länge des Liedes": "4:32",
    "Streams auf Spotify": 150560966
}


def guess_song_description_english(key, value):
    return key in song_description_english and value == song_description_english[key]


def guess_song_description_german(key, value):
    return key in song_description_german and value == song_description_german[key]


def play_english_game():
    while True:
        key = input("Type in the attribute:\n")
        if is_exit(key):
            break
        value = input("Type in your guess:\n")
        if is_exit(value):
            break
        res = guess_song_description_english(key, value)
        print(res)


def play_german_game():
    while True:
        key = input("Wähle ein Attribut:\n")
        if is_exit(key):
            break
        value = input("Gebe deine Lösung ein:\n")
        if is_exit(value):
            break
        res = guess_song_description_german(key, value)
        print(res)


def is_exit(key):
    return key == "Exit" or key == "exit" or key == "EXIT"


def print_english_manual():
    print("In this game you can guess the answer of the following attributes:\n"
          "Song, Artist, Genre, Album, Release Year, Duration or Spotify Streams\n"
          "How to play:\n"
          "\t1. Type in one of the attributes\n"
          "\t2. Type in your guess\n"
          "If your guess was RIGHT it will say True and you can play again\n"
          "If your guess was WRONG it will say False and you can play again\n"
          "If you want to exit the game or see the solutions type in Exit\n"
          "Have fun!")
    play_english_game()
    return True


def print_german_manual():
    print("Bei diesem Spiel kannst du die Lösung folgender Attribute raten:\n"
          "Song, Künstler, Genre, Album, Erscheinungsjahr, Länge des Liedes oder Streams auf Spotify\n"
          "Erklärung:\n"
          "\t1. Wähle einen der oben aufgezählten Attribute und bestätige ihn mit Enter.\n"
          "\t2. Gebe deine Lösung ein.\n"
          "Wenn deine Antwort richtig war, wird True ausgegeben und das Spiel startet von vorne.\n"
          "Wenn deine Antwort falsch war, wird False ausgegeben und das Spiel startet von vorne.\n"
          "Wenn du das Spiel verlassen willst, oder die Lösungen sehen willst, gebe Exit ein.\n"
          "Viel Spaß!")
    play_german_game()
    return True


def choose_language():
    global language
    language = input("Type in english and press enter for the english manual.\n"
                     "Type in german and press enter for the german manual.\n")
    if language in languages[0:5]:
        print_english_manual()
    elif language in languages[6:11]:
        print_german_manual()


def print_english_solution():
    for key in song_description_english:
        print(key, ":", song_description_english[key])


def print_german_solution():
    for key in song_description_german:
        print(key, ":", song_description_german[key])


choose_language()

if language in languages[0:5]:
    print_english_solution()

if language in languages[6:11]:
    print_german_solution()
