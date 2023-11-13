from random import choice
def own():
    return choice(input("Which series ? ").split(","))

def generator():
    list =["Naruto", "Demon Slayer", "JoJo's Bizzare Adventure", "Jujutsu Kaisen", "One Piece", "Fate Series"]
    return choice(list)

def main():
    command = input("Which command? ")
    if command == "own":
        return own()
    elif command == "generator":
        return generator()
    else:
        print("No command found")

if __name__ == "__main__":
    print(main())