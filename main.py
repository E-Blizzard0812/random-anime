from random import choice
def e():
    list =["Naruto", "Demon Slayer", "JoJo's Bizzare Adventure", "Jujutsu Kaisen", "One Piece", "Fate Series"]
    return choice(list)

def main():
    return e()

if __name__ == "__main__":
    print(main())