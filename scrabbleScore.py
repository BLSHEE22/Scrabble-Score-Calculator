import sys
import re

def main():

    def prompt():
        print("Would you like to input a word/phrase or read in a file?\n")
        choice = input("(Answer either 'input' or 'file'.)\n\n")
        return choice
            
    def readInFile(name):

        with open(name) as f:
            lines = f.readlines()

        return lines

    print("\nWelcome to Scrabble Score Evaluator!\n")

    while (True):
        ans = prompt()
        if ans.lower == "quit":
            print("\nQuitting...\n")
            quit()
        elif ans.lower() == "input":
            i = input("\nEnter a word or phrase to be evaluated.\n\n")
            lines = [i]
            break
        elif ans.lower() == "file":
            f = input("\nWhich file would you like to be read in?\n\n")
            lines = readInFile(f)
            break
        else:
            print("\nI'm sorry, I didn't quite get that.\n")

    scrabble = {
            'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2,
            'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3,
            'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4,
            'w':4, 'x':8, 'y':4, 'z':10
            }

    print()

    namePtLst = []

    lines = [re.sub(r"[\n\t\s\'-]*", "", x).lower() for x in lines]

    for x in lines:
        namePts = sum([scrabble[y] for y in x])
        namePtLst.append(namePts)

    for z in namePtLst:
        print(z)
    
    print()

if __name__ == "__main__":
    main()
