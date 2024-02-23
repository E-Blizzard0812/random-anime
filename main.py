import pandas as pd
#import jikan
import timeit
import random

def own():
    return choice(input("Which series ? ").split(","))

def generator():
    dict = {
        "N": "Naruto", 
        "DS": "Demon Slayer", 
        "J" : "JoJo's Bizzare Adventure", 
        "JJK" : "Jujutsu Kaisen", 
        "OP": "One Piece", 
        "FS": "Fate Series",
        "M" : "Mashle",
        "COE" : "Classroom of the Elite",
        "DAL" : "Date a Live",
        "" : "" 
    }
    return (random.sample(sorted(dict.items()), 1))[0][1]

def liste():
    liste = ["Naruto", "Demon Slayer","JoJo's Bizzare Adventure", "Jujutsu Kaisen", "One Piece", "Fate Series","Mashle","Classroom of the Elite" ]
    return random.choice(liste)

def main():
    command = input("Which command? ")
    match command:
        case "own":
            return own()
        case "g": 
            return generator()
        case _:
            print("No command found")

generator_time = timeit.timeit(lambda: generator(), number = 1000)
liste_time = timeit.timeit(lambda: liste(), number = 1000 )

if __name__ == "__main__":
    #print(main()+f" took {generator_time} seconds and {liste_time} seconds")
    print(f"You should watch {main()}.")
    #print(type(main()))