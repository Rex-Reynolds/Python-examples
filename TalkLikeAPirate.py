#Rex Reynolds
#Talk like a Pirate

#create the dicitonary from English to Pirate
def createDictionary():
    pirate_dict = {}
    with open("Translation.txt",'r') as file:
        for line in file:
            line = line.strip()
            linelist = line.split(":")
            pirate_dict[linelist[0]] = linelist[1]
        return pirate_dict


#Read the input and do the printing loop
#Takes the English to pirate dictionary as input.

def readInput(aDict):
    from random import randrange
    import re
    print("Arr! Welcome to the Pirate translator!")
    user = input("Enter a line: ")
    whitelist = ['this']
    splitUser = user.split()
    rand = randrange(10)
    while user != "quit":
        for word in aDict:
            user = re.sub(r"\b"+word+r"\b", aDict[word],user)
        print("Translation:", user)
        user = input("Enter a line: ")
        rand = randrange(10)
def main():
    the_dict = createDictionary()
    readInput(the_dict)

main()
