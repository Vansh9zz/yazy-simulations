import random

def cont():
    print("Press Enter to continue: ")

def roll(dice, diceLocked, numRolls):

    for i in range(5):

        if not diceLocked[i]:
            dice[i] = random.randint(1,6)

    
    print(f"Roll {numRolls}/3:", end = " ")
    
    for i in range(5):
        print(dice[i], end = " ")

    print()

    return dice

def lockDice(diceLocked):

    prompt = list(map(int,input("Which dice do you want to lock? (Space Separated): ").split(" ")))
    prompt = [prompt[i] - 1 for i in range(len(prompt))]

    for i in range(5):
        if (i in prompt):
            diceLocked[i] = True
        else:
            diceLocked[i] = False

    return diceLocked


def checkCategories(dice, scoreTaken, scores, availableScores):

    s = sum(dice)
    map = [0 for i in range(6)]
    sortedDies = sorted(dice)

    for i in range(5):
        map[dice[i]-1] += 1

    ## Category 1 - 6
    for idx in range(6):
        if not scoreTaken[idx]:
            availableScores[idx] = map[idx] * (idx + 1)

    ## Category 7 - AAA
    if not scoreTaken[6] and max(map) >= 3:
        availableScores[6] = s

    ## Category 8 - AAAA
    if not scoreTaken[7] and max(map) >= 4:
        availableScores[7] = s

    ## Category 9 - AAABB
    if not scoreTaken[8] and 3 in map and 2 in map:
        availableScores[8] = 25

    ## Category 10 - ABCDE
    if not scoreTaken[9] and (sortedDies == [1,2,3,4,5] or sortedDies == [2,3,4,5,6]):
        availableScores[9] = 40

    ## Category 11 - AAAAA
    if not scoreTaken[10] and 5 in map:
        availableScores[10] = 50

    print(f"\n CURRENT SCORE: {currScore}")
    print("\n====== Available Scores ======")

    categories = [
        "Ones",
        "Twos",
        "Threes",
        "Fours",
        "Fives",
        "Sixes",
        "AAA",
        "AAAA",
        "AAABB",
        "ABCDE",
        "AAAAA"
    ]

    for i in range(11):
        if not scoreTaken[i]:
            print(f"{i+1 :2}. {categories[i]:20} : {availableScores[i]}")
        else:
            print(f"{i+1 :2}. {categories[i]:20} : TAKEN ({scores[i]})")

    print("\n==============================")

    return availableScores

    

def pickCategory(scores, scoreTaken, numTurns, diceLocked, dice, numRolls, availableScores):

    global currScore

    choice = int(input("Which category do you choose?: "))

    scores[choice - 1] = availableScores[choice - 1]
    scoreTaken[choice - 1] = True
    
    print(f"END OF TURN {numTurns}")

    currScore += scores[choice-1]

    return scores


currScore = 0

def run():

    '''
    
    CATEGORIES:

    01. ONES - No of ones
    02. TWOS - No of twos
    03. THREES - No of threes
    04. FOURS - No of fours
    05. FIVES - No of fives
    06. SIXES - No of sixes
    07. AAA
    08. AAAA
    09. AAABB
    10. ABCDE
    11. AAAAA
    12. Lucky Number (later)    
    
    '''
    global currScore

    dice = [0 for i in range(5)]
    diceLocked = [False for i in range(5)]
    numRolls = 1

    scores = [0 for i in range(11)]
    scoreTaken = [False for i in range(11)]
    availableScores = [0 for i in range(11)]

    numTurns = 1

    while numTurns <= 11:

        '''
        
        In one turn, we can:

        - Roll dies
        - Choose locked dies and reroll (total of 3 rolls)
        - Pick a category

        What all do we get from the simulation in this turn:

        - Dies rolled
        - Available scores after every roll

        
        '''

        diceLocked = [False for i in range(5)]
        dice = [0 for i in range(5)]
        numRolls = 1
        availableScores = [0 for i in range(11)]

        print(f"TURN {numTurns}/11")
        while numRolls <= 3:

            dice = roll(dice, diceLocked, numRolls)
            

            availableScores = checkCategories(dice, scoreTaken, scores, availableScores)

            if numRolls != 3:
                choice = int(input("Do you want to lock dice or pick a category? (0 for Locking Dies, 1 for Categories): "))

                if choice == 0:
                    diceLocked = lockDice(diceLocked)
                else:
                    scores = pickCategory(scores, scoreTaken, numTurns, diceLocked, dice, numRolls, availableScores)
                    numTurns += 1
                    break
            else:
                scores = pickCategory(scores, scoreTaken, numTurns, diceLocked, dice, numRolls, availableScores)
                numTurns += 1

            numRolls += 1

    print(f"\n Your final score was {currScore}")

            
if __name__ == "__main__":
    run()
        
