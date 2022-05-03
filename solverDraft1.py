from operator import truediv
import sys, getopt # DELETE second

debug = True
# debug = False

originalPuzzle = []

def printOriginalPuzzle():

    # if debug: print(originalPuzzle) # DEBUG

    for i in range(len(originalPuzzle)):

        for j in range(len(originalPuzzle[i])-1):

            print(originalPuzzle[i][j], end = " ")

        if i < len(originalPuzzle) - 1:

            print(originalPuzzle[i][-1])

        else:

            print(originalPuzzle[i][-1], end = "")



def loadPuzzle(puzzlePath):

    global originalPuzzle

    with open(puzzlePath, "r") as puzzleFile:

        puzzleLines = puzzleFile.readlines()

    for i in range(len(puzzleLines)):

        # puzzleLines[i].split()
        # if debug: print(puzzleLines[i], end = "") # DEBUG
        nextPuzzleLine = []

        for j in puzzleLines[i]:

            if j.isdigit():

                nextPuzzleLine.append(j)


        originalPuzzle.append(nextPuzzleLine)

            # print(puzzleLines[i][j], end= " ")

    if debug: printOriginalPuzzle()



def sudokuSolver():

    if len(sys.argv) != 2:

        # print('arguments: ', sys.argv) # DEBUG
        userInput = input("Please enter path to puzzle file: ")
        loadPuzzle(userInput)

    else:

        loadPuzzle(sys.argv[1])



def main():

    # printInput(sys.argv)
    sudokuSolver()


if(__name__ == '__main__'):
    main()