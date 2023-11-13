from random import choice
command = input("Which command? ")

def own():
    userlist = input("Which series ? ")
    userlist = userlist.split(",")
    return choice(userlist)

def generator():
    list =["Naruto", "Demon Slayer", "JoJo's Bizzare Adventure", "Jujutsu Kaisen", "One Piece", "Fate Series"]
    return choice(list)

def main():
    if command == "own":
        return own()
    elif command == "generator":
        return generator()
    else:
        print("No command found")

if __name__ == "__main__":
    print(main())