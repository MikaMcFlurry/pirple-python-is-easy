import os.path

filename = input("Type in your filename: \n")
if os.path.isfile(filename) == True:
    action =  input("Do you want to \n A) Read the file (type A) \n B) Delete the file and start over (type B) \n C) Append the file (type C) \n D) Append the file (type D)\n") 
    if action == "A":
        file = open(filename, "r")
        print(file.read())
        file.close()
    elif action == "B":
        file = open(filename, "w")
        file.write(input("Type in your note here:\n"))
        file.close
    elif action == "C":
        file = open(filename, "a")
        file.write(input("Type in your note here:\n"))
        file.close
    elif action == "D":
        file = open(filename, "r")
        list_of_lines = file.readlines()
        line = input("Wich line do you want to change?\n")
        list_of_lines[line] = input("Type in your replacement here:\n")
        file.close

        file = open(filename, "w")
        file.writelines(list_of_lines)
        file.close
    else:
        print("Type in a valid letter!")
else:
    file = open(filename, "w")
    file.write(input("Type in your note here:\n"))
    file.close

        


