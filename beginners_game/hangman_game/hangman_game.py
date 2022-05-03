import random
from words import words


def generateHangman():
    print("        O")
    print("       \\  /")
    print("        |")
    print("       / \\")

def getRandomWord():
    return words[random.randint(0,len(words))]

word = getRandomWord()
print(word)
generateHangman()
