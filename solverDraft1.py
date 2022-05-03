import sys, getopt # DELETE second
import math
import copy
# import numpy as np


debug = True
debug = False


def printPuzzle(printablePuzzle):

    # if debug: print(printablePuzzle) # DEBUG

    for i in range(len(printablePuzzle)):

        for j in range(len(printablePuzzle[i])-1):

            print(printablePuzzle[i][j], end = " ")

        if i < len(printablePuzzle) - 1:

            print(printablePuzzle[i][-1])

        else:

            print(printablePuzzle[i][-1], end = "")


def loadPuzzle(puzzlePath):

    originalPuzzle = []

    with open(puzzlePath, "r") as puzzleFile:

        puzzleLines = puzzleFile.readlines()

    for i in range(len(puzzleLines)):

        # puzzleLines[i].split()
        # if debug: print(puzzleLines[i], end = "") # DEBUG
        nextPuzzleLine = []

        for j in puzzleLines[i]:

            if j.isdigit():

                nextPuzzleLine.append((int)(j))


        originalPuzzle.append(nextPuzzleLine)

            # print(puzzleLines[i][j], end= " ")

    if debug: printPuzzle(originalPuzzle)

    return originalPuzzle


def getBlocks(linePuzzle):

    # Convert puzzle organized by rows into puzzle organized by 3x3 blocks

    # puzzleBlocks = [[0] * 9] * 9
    puzzleBlocks = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], ]

    # pCount = -1
    # iOffset = -3


    
    for i in range(len(linePuzzle)):

        # if i % 3 == 0:
        #     iOffset += 3

        # jOffset = -1
        for j in range(len(linePuzzle[i])):


            # if j % 3 == 0:

            #     jOffset += 1

            # print("i: " + str(i) + " j: " + str(j))
            # print("iOffset: " + str(iOffset) + " jOffset: " + str(jOffset))
            # print("linePuzzle[i][j]: " + str(linePuzzle[i][j]))

            # puzzleBlocks[iOffset + jOffset][(3 * (i % 3)) + (j % 3)] = linePuzzle[i][j]
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

    curPuzzle = copy.copy(ogPuzzle)
    # possiblePuzzle = copy.copy(curPuzzle)
    # unsolved = []
    if lastCount == None:
        lastCount = 0

    unsolvedCount = 0
    # ogBlocks = getBlocks(ogPuzzle)
    # print(ogBlocks) # TEMP

    # Do an initial sweep, replacing all 0s with all possible notes

    # for i in range(len(possiblePuzzle)):
    for i in range(len(curPuzzle)):

        # for j in range(len(possiblePuzzle[i])):
        for j in range(len(curPuzzle[i])):

            # if possiblePuzzle[i][j] == 0:
            if curPuzzle[i][j] == 0:

                unsolvedCount += 1

                



                # unsolved.append([i, j]) # TODO

                possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                # for testVal in range(9):
                for testVal in range(1, 10):

                    if check(curPuzzle, i, j, testVal) == False:

                        if testVal in possibleValues:
                            possibleValues.remove(testVal)
                        

                        # possiblePuzzle[i][j].append(testVal)

                        # if 0 in possiblePuzzle[i][j]:

                        #     possiblePuzzle[i][j].remove(0)

                # print("(" + str(i) + ", " + str(j) + "): ", end = "")
                # print(possibleValues)

                if len(possibleValues) == 1:

                    curPuzzle[i][j] = copy.copy(possibleValues[0])
                    unsolvedCount -= 1
                    # unsolved.remove([i, j])
                    # i = 0
                    # j = 0
                    # break
                # elif blockNum(i, j) == 0:

                #     tempBlock = getBlocks(curPuzzle)
                #     print(tempBlock[0])

                    # else: # NOTE may not be necessary, could just recopy curPuzzle

                    #     if testVal in possiblePuzzle[i][j]:

                    #         possiblePuzzle[i][j].remove(testVal)

                # if len(possiblePuzzle[i][j]) == 2: # TODO may want to tab right

                    # curPuzzle[i][j] = copy.copy(possiblePuzzle[i][j][1])
                    # i = 0
                    # break

    if unsolvedCount > 0:

        if unsolvedCount == lastCount:

            print("Something went wrong")
            printPuzzle(curPuzzle)
            quit()

        else:

            solver(curPuzzle, unsolvedCount)

    else:

        printPuzzle(curPuzzle)
        quit()

    # i = 0
    # while len(unsolved) != 0:

        # unsolved[i]

    # for i in range(len(curPuzzle)):

    #     for j in range(len(curPuzzle[i])):

    #         if curPuzzle[i][j] == 0:

    #             possibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    #             for testVal in range(1, 10):

    #                 if check(curPuzzle, i, j, testVal) == False:

    #                     if testVal in possibleValues:
    #                         possibleValues.remove(testVal)
                        

    #                     # possiblePuzzle[i][j].append(testVal)

    #                     # if 0 in possiblePuzzle[i][j]:

    #                     #     possiblePuzzle[i][j].remove(0)

    #             print("(" + str(i) + ", " + str(j) + "): ", end = "")
    #             print(possibleValues)



    printPuzzle(curPuzzle)

                













def sudokuSolverMain():

    if len(sys.argv) != 2:

        # print('arguments: ', sys.argv) # DEBUG
        userInput = input("Please enter path to puzzle file: ")
        loadPuzzle(userInput)

    else:

        solver(loadPuzzle(sys.argv[1]))



def main():

    # printInput(sys.argv)
    sudokuSolverMain()


if(__name__ == '__main__'):
    main()