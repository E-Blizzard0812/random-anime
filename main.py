#import pandas as pd
import timeit
import random
from random import sample
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
        "COE" : "Classroom of the Elite"       
    }
    rs =  random.sample(sorted(dict.items()), 1)
    return rs[0][1]

def main():
    command = input("Which command? ")
    match command:
        case "own":
            return own()
        case "g": 
            return generator()
        case _:
            print("No command found")

def runtime():
    generator_time = timeit.timeit(lambda: generator(), number = 1000)

if __name__ == "__main__":
    print(main()+f" took {generator_time} seconds")
    #print(main())
    #print(type(main()))