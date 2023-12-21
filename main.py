#import pandas as pd
import timeit
import random
from random import choice
def own():
    return choice(input("Which series ? ").split(","))

def generator():
    list =["Naruto", "Demon Slayer", "JoJo's Bizzare Adventure", "Jujutsu Kaisen", "One Piece", "Fate Series"]
    return choice(list)

def betterg():
    dict = {
        "N": "Naruto", 
        "DS": "Demon Slayer", 
        "J" : "JoJo's Bizzare Adventure", 
        "JJK" :"Jujutsu Kaisen", 
        "OP": "One Piece", 
        "FS":"Fate Series"       
    }
    return random.sample(dict.items(), 1)

def main():
    command = input("Which command? ")
    match command:
        case "own":
            return own()
        case "g": 
            return generator()
        case "bg":
            return betterg()
        case _:
            print("No command found")

generator_time = timeit.timeit(lambda: generator(), number = 1000)
betterg_time = timeit.timeit(lambda: betterg(), number = 1000)

if __name__ == "__main__":
    print(main()+f" took {generator_time} seconds")
    print(main()+f" took {betterg_time} seconds")