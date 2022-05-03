import random
from words import words


def generateHangman(number = 6):
    first = "        O"
    second = "       \\"
    third = "         /"
    fourth = "        |"
    fifth = "       /"
    sixth = "       \\"
    dict = {1: first, 2: second, 3: third, 4: fourth, 5: fifth, 6: sixth}
    if number <= 6:
        print("lost turn")
        print(dict.get(number))
    else:
        print("You have lost all You Chances !")
        for i in range(7):
            print(dict.get(i))


def getRandomWord():
    return words[random.randint(0, len(words))]


def generateBlindedUnderscore(word):
    displaying = ""
    for i in range(len(word)):
        displaying += "_"
    return displaying


def findInWord(letter, word):
    return letter in word


def displayWithEachLetter(letter, word, finalLength):
    displaying = ""
    for i in range(len(word)):
        if word[i] == letter:
            displaying += letter
            finalLength +=1
        else:
            displaying += "_"
    print(displaying)
    return finalLength


def getUserInput():
    choice = str(input("choose one letter: "))
    length = len(choice)
    while length >= 2:
        choice = str(input("choose only one letter: "))
        length = len(choice)
    return choice






word = getRandomWord()
print(f"the word is {word} and his lentgh is {len(word)}")

display = generateBlindedUnderscore(word)
print(display)

cpt = 1
choice = str(input("choose one letter: "))
length = len(choice)

finalLength = 0

while cpt <= 6:
    while length >= 2:
        choice = str(input("choose only one letter: "))
        length = len(choice)

    result = findInWord(choice, word)
    if result:
        finalLength = displayWithEachLetter(choice, word, finalLength)
        #print(f" final length is actually {finalLength}")
        if finalLength == len(word):
            cpt = 6
            print(f"Congratulations You've find the word : {word}")
            break
        else:
            choice = getUserInput()
    else:
        generateHangman(cpt)
        cpt += 1
        choice = getUserInput()


if cpt>6:
    generateHangman(cpt)