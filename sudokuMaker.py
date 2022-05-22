import sys
import math
import copy
import random

debug = True
# debug = False

guessMask = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]



def printPuzzle(printablePuzzle):

    for i in range(len(printablePuzzle)):

        for j in range(len(printablePuzzle[i])-1):

            print(printablePuzzle[i][j], end = " ")

        if i < len(printablePuzzle) - 1:

            print(printablePuzzle[i][-1])

        else:

            print(printablePuzzle[i][-1], end = "")



def getBlocks(linePuzzle):

    # Convert puzzle organized by rows into puzzle organized by 3x3 blocks

    puzzleBlocks = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(len(linePuzzle)):

        for j in range(len(linePuzzle[i])):


            # if j % 3 == 0:

            #     jOffset

          
           

           
            puzzleBlocks[(3 * math.floor(i / 3)) + math.floor(j / 3)][(3 * (i % 3)) + (j % 3)] = copy.copy(linePuzzle[i][j])

    # puzzleBlocks[0][0] = linePuzzle[0][0]

    return puzzleBlocks



def blockNum(row, col):

    return (3 * math.floor(row / 3)) + math.floor(col / 3)



def possibleCheck(group, value):

    # Check if the value already exists in the specified row, column, or 3x3 block
    for i in group:

        if i == value:

            return False

    return True



def check(currentPuzzle, row, col, value):

    # Prepare the information to be checked for all 3 tests by possibleCheck()
    check1 = False
    check2 = False
    check3 = False

    # Check if the value already exists in the row
    check1 = possibleCheck(currentPuzzle[row], value)

    # Check if the value already exists in the column
    columnValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(columnValues)):
        columnValues[i] = copy.copy(currentPuzzle[i][col])
    check2 = possibleCheck(columnValues, value)

    # Check if the value already exists in the block
    puzzleBlock = getBlocks(currentPuzzle)
    blockIndex = blockNum(row, col)
    # if blockIndex == 0:
        # print(value)
        # print(puzzleBlock[blockIndex])
    check3 = possibleCheck(puzzleBlock[blockIndex], value)

    # if check1 == False or check2 == False or check3 == False:

    #     return False

    if check1 == True and check2 == True and check3 == True:
        # print(row)
        # print(col)
        # print(value)
        return True
    else:
        return False


def solver(ogPuzzle, lastCount = None):

    global guessMask
    curPuzzle = copy.deepcopy(ogPuzzle)
    if lastCount == None:
        lastCount = 0
    unsolvedCount = 0
    minValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    minX = 0
    minY = 0

    # Do an initial sweep, replacing all 0s with all possible notes
    for i in range(len(curPuzzle)):

        for j in range(len(curPuzzle[i])):

            if curPuzzle[i][j] == 0:

                unsolvedCount += 1
                possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                for testVal in range(1, 10):

                    if check(curPuzzle, i, j, testVal) == False:

                        if testVal in possibleValues:

                            possibleValues.remove(testVal)

                if len(possibleValues) == 1:

                    curPuzzle[i][j] = copy.copy(possibleValues[0])
                    unsolvedCount -= 1

                elif len(possibleValues) < len(minValues):

                    minX = i
                    minY = j
                    minValues = copy.deepcopy(possibleValues)

    if unsolvedCount > 0 and unsolvedCount != lastCount:

        # If there is still unsolved cells and the most recent run was an improvement, then run it again
        return solver(curPuzzle, unsolvedCount)
        # print("Program should never reach here") # DEBUG
        # quit()

    elif unsolvedCount == 0:

        # If there are no unsolved cells left, then the puzzle has been solved
        if debug: printPuzzle(curPuzzle)
        if debug: print("Solved!") # DEBUG
        return True

    elif unsolvedCount == lastCount:

        # If there has been no improvement in the most recent run, then begin guessing algorithm
        if debug: printPuzzle(curPuzzle) # DEBUG

        for guessValue in minValues:

            if debug: print("\n[" + str(minX) + "][" + str(minY) + "]: " + str(guessValue)) # DEBUG
            # print(guessValue) # DEBUG

            guessPuzzle = copy.deepcopy(curPuzzle)
            guessPuzzle[minX][minY] = guessValue
            # guesser(guessPuzzle, unsolvedCount - 1)
            output = solver(guessPuzzle, unsolvedCount - 1)

            # if output == False:
                # guessMask[minX][minY] = 0
            if output == True:
                guessMask[minX][minY] = guessValue


            return output


def puzzleTester(testPuzzle = None):

    if testPuzzle == None:

        testPuzzle = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for i in range(9):

            modX = random.randrange(1, 9, 1)
            modY = random.randrange(1, 9, 1)

            while testPuzzle[modX][modY] != 0:

                modX = random.randrange(1, 9, 1)
                modY = random.randrange(1, 9, 1)

            possibleNewVals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            for newVal in range(1, 10):

                if check(testPuzzle, modX, modY, newVal) == False:

                    if newVal in possibleNewVals:

                        possibleNewVals.remove(newVal)

            if len(possibleNewVals) == 0:

                return False

            updateVal = random.choice(possibleNewVals)

            testPuzzle[modX][modY] = updateVal


    if solver(copy.deepcopy(testPuzzle)) == True:

        for i in range(len(guessMask)):

            for j in range(len(guessMask[i])):

                if guessMask[i][j] != 0:

                    testPuzzle[i][j] = guessMask[i][j]

        print("\nPuzzle:")
        printPuzzle(testPuzzle)
        print("\nMask:")
        printPuzzle(guessMask)
        print("\n")
        quit()
        return True

    else:


        modX = random.randrange(1, 9, 1)
        modY = random.randrange(1, 9, 1)

        while testPuzzle[modX][modY] != 0:

            modX = random.randrange(1, 9, 1)
            modY = random.randrange(1, 9, 1)

        possibleNewVals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for newVal in range(1, 10):

            if check(testPuzzle, modX, modY, newVal) == False:

                if newVal in possibleNewVals:

                    possibleNewVals.remove(newVal)

        if len(possibleNewVals) == 0:

            return False

        updateVal = random.choice(possibleNewVals)

        testPuzzle[modX][modY] = updateVal

        puzzleTester(testPuzzle)





# def sudokuSolverMain():

#     if len(sys.argv) != 2:

#         # print('arguments: ', sys.argv) # DEBUG
#         userInput = input("Please enter path to puzzle file: ")
#         loadPuzzle(userInput)

#     else:

#         solver(loadPuzzle(sys.argv[1]))



def main():

    # printInput(sys.argv)

    test = False

    while test != True:

        test = puzzleTester()
        # test = puzzleTester([[0, 5, 1, 0, 0, 0, 0, 3, 0], [0, 3, 7, 0, 4, 8, 2, 9, 5], [9, 4, 8, 5, 2, 0, 6, 0, 7], [0, 6, 9, 3, 1, 0, 7, 0, 0], [0, 0, 0, 2, 8, 9, 3, 4, 6], [8, 2, 0, 0, 6, 0, 0, 0, 1], [7, 0, 6, 0, 0, 2, 0, 0, 9], [3, 0, 4, 8, 5, 6, 1, 7, 2], [5, 8, 2, 9, 0, 0, 4, 0, 3]])
        # test = puzzleTester([[0, 5, 1, 0, 0, 0, 0, 3, 0], [0, 3, 7, 0, 4, 8, 2, 9, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 8, 9, 3, 4, 6], [8, 2, 0, 0, 6, 0, 0, 0, 1], [7, 0, 6, 0, 0, 2, 0, 0, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 8, 2, 9, 0, 0, 4, 0, 3]])



if(__name__ == '__main__'):
    main()
