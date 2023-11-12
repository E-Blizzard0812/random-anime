from random import choice
def generator():
    list =["Naruto", "Demon Slayer", "JoJo's Bizzare Adventure", "Jujutsu Kaisen", "One Piece", "Fate Series"]
    return choice(list)

def main():
    return generator()

if __name__ == "__main__":
    print(main())